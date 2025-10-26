# Wymagane biblioteki
library(smoof)
library(ggplot2)
library(dplyr)

# Funkcja pomocnicza do konwersji domeny
convert_domain <- function(par_set) {
  lapply(par_set, function(param) c(param$lower, param$upper))
}

# Funkcja pomocnicza do uruchamiania PRS
pure_random_search <- function(fun, domain, budget) {
  best_value <- Inf
  
  for (i in 1:budget) {
    # Generowanie punktu losowego
    point <- sapply(domain, function(d) runif(1, d[1], d[2]))
    # Debugowanie: Sprawdź długość punktu
    if (length(point) != length(domain)) {
      stop("Długość punktu nie zgadza się z długością domeny.")
    }
    # Obliczanie wartości funkcji
    value <- fun(point)
    # Aktualizacja najlepszego wyniku
    if (value < best_value) {
      best_value <- value
    }
  }
  return(best_value)
}

# Funkcja pomocnicza do uruchamiania MS
multi_start <- function(fun, domain, n_starts) {
  best_value <- Inf
  
  for (i in 1:n_starts) {
    # Generowanie punktu startowego
    start_point <- sapply(domain, function(d) runif(1, d[1], d[2]))
    # Debugowanie: Sprawdź długość punktu startowego
    if (length(start_point) != length(domain)) {
      stop("Długość punktu startowego nie zgadza się z długością domeny.")
    }
    
    # Optymalizacja lokalna
    result <- optim(
      par = start_point,  # Punkt startowy
      fn = fun, 
      method = "L-BFGS-B", 
      lower = sapply(domain, `[[`, 1), 
      upper = sapply(domain, `[[`, 2)
    )
    # Aktualizacja najlepszego wyniku
    if (result$value < best_value) {
      best_value <- result$value
    }
  }
  return(best_value)
}

# Przygotowanie funkcji testowych
functions <- list(
  rastrigin = makeRastriginFunction,
  alpine01 = makeAlpine01Function
)

# Budżet i liczba powtórzeń
n_repeats <- 50
budget <- 1000  # PRS
n_starts <- 100  # MS

# Przygotowanie danych dla różnych wymiarów
dimensions <- c(2, 10, 20)
results <- list()

for (dim in dimensions) {
  for (fun_name in names(functions)) {
    # Tworzenie funkcji dla danego wymiaru
    fun <- functions[[fun_name]](dimensions = dim)
    domain <- convert_domain(getParamSet(fun)$pars)
    
    # Debugowanie: Sprawdź domenę
    cat("Funkcja:", fun_name, "Wymiary:", dim, "\n")
    cat("Domena:", toString(domain), "\n")
    
    # PRS
    prs_values <- replicate(n_repeats, pure_random_search(fun, domain, budget))
    
    # MS
    ms_values <- replicate(n_repeats, multi_start(fun, domain, n_starts))
    
    # Zapis wyników
    results[[paste(fun_name, dim, "PRS", sep = "_")]] <- prs_values
    results[[paste(fun_name, dim, "MS", sep = "_")]] <- ms_values
  }
}

# Wizualizacja wyników
plot_results <- function(data, title) {
  ggplot(data, aes(x = Algorithm, y = Value, fill = Algorithm)) +
    geom_boxplot() +
    labs(title = title, y = "Minimum Value", x = "Algorithm") +
    theme_minimal()
}

# Przykładowe wykresy
for (dim in dimensions) {
  for (fun_name in names(functions)) {
    # Przygotowanie danych
    prs_key <- paste(fun_name, dim, "PRS", sep = "_")
    ms_key <- paste(fun_name, dim, "MS", sep = "_")
    
    data <- data.frame(
      Algorithm = rep(c("PRS", "MS"), each = n_repeats),
      Value = c(results[[prs_key]], results[[ms_key]])
    )
    
    # Tworzenie wykresu
    plot_title <- paste0(toupper(substr(fun_name, 1, 1)), substr(fun_name, 2, nchar(fun_name)),
                         " Function (", dim, " Dimensions)")
    print(plot_results(data, plot_title))
  }
}

# Analiza statystyczna
for (dim in dimensions) {
  for (fun_name in names(functions)) {
    prs_key <- paste(fun_name, dim, "PRS", sep = "_")
    ms_key <- paste(fun_name, dim, "MS", sep = "_")
    
    prs_values <- results[[prs_key]]
    ms_values <- results[[ms_key]]
    
    # Test t-Studenta
    t_test <- t.test(prs_values, ms_values)
    
    # Przedziały ufności
    prs_ci <- t.test(prs_values)$conf.int
    ms_ci <- t.test(ms_values)$conf.int
    
    # Wyniki
    cat("Funkcja:", fun_name, "Wymiary:", dim, "\n")
    cat("PRS - Średnia:", mean(prs_values), "CI:", prs_ci, "\n")
    cat("MS - Średnia:", mean(ms_values), "CI:", ms_ci, "\n")
    cat("Test t-Studenta (p-value):", t_test$p.value, "\n\n")
  }
}