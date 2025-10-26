library(smoof)
library(rlist)

calcMS <- function(points, dimensions, lowerBound, upperBound, fn) {
  msRes <- replicate(points, optim(runif(dimensions, min = lowerBound, max = upperBound), fn, method = "L-BFGS-B",
                                   lower = rep(lowerBound, dimensions), upper = rep(upperBound, dimensions)))
  calls <- c()
  for (i in seq_along(msRes[3,])){
    calls <- append(calls, msRes[3,][[i]]["function"])
  }
  minVal <- min(unlist(msRes[2,]))
  return (c(minVal, sum(calls)))
}

prs <- function(fn, points) {
  minVal <- Inf
  for (i in seq_along(points)) {
    value <- fn(points[[i]])
    minVal <- min(minVal, value) }
  return (minVal)
}

generatePoints <- function(n, dimensions, lower, upper) {
  res <- list()
  for (i in 1:n) {
    res <- list.append(res, runif(dimensions, min = lower, max = upper)) }
  return (res)
}

compar <- function(fn, dimensions, bounds) {
  msRes <- replicate(100, calcMS(100, dimensions, bounds[1], bounds[2], fn))
  msValue <- msRes[1,]
  budget <- round(mean(msRes[2,]))

  prsValue <- replicate(100, prs(fn, generatePoints(budget, dimensions, bounds[1], bounds[2])))
  return (list(msValue, prsValue))
}

alpine01Bounds <- c(-10.0, 10.0)
alpine012D <- compar(makeAlpine01Function(2), 2, alpine01Bounds)
alpine012Dms <- alpine012D[[1]]
alpine012Dprs <- alpine012D[[2]]
write.csv(alpine012Dms, file = "./data/alpine012Dms.csv", row.names = FALSE)
write.csv(alpine012Dprs, file = "./data/alpine012Dprs.csv", row.names = FALSE)

alpine0110D <- compar(makeAlpine01Function(10), 10, alpine01Bounds)
alpine0110Dms <- alpine0110D[[1]]
alpine0110Dprs <- alpine0110D[[2]]
write.csv(alpine0110Dms, file = "./data/alpine0110Dms.csv", row.names = FALSE)
write.csv(alpine0110Dprs, file = "./data/alpine0110Dprs.csv", row.names = FALSE)

alpine0120D <- compar(makeAlpine01Function(20), 20, alpine01Bounds)
alpine0120Dms <- alpine0120D[[1]]
alpine0120Dprs <- alpine0120D[[2]]
write.csv(alpine0120Dms, file = "./data/alpine0120Dms.csv", row.names = FALSE)
write.csv(alpine0120Dprs, file = "./data/alpine0120Dprs.csv", row.names = FALSE)

rastriginBounds <- c(-5.12, 5.12)
rastrigin2D <- compar(makeRastriginFunction(2), 2, rastriginBounds)
rastrigin2Dms <- rastrigin2D[[1]]
rastrigin2Dprs <- rastrigin2D[[2]]
write.csv(rastrigin2Dms, file = "./data/rastrigin2Dms.csv", row.names = FALSE)
write.csv(rastrigin2Dprs, file = "./data/rastrigin2Dprs.csv", row.names = FALSE)

rastrigin10D <- compar(makeRastriginFunction(10), 10, rastriginBounds)
rastrigin10Dms <- rastrigin10D[[1]]
rastrigin10Dprs <- rastrigin10D[[2]]
write.csv(rastrigin10Dms, file = "./data/rastrigin10Dms.csv", row.names = FALSE)
write.csv(rastrigin10Dprs, file = "./data/rastrigin10Dprs.csv", row.names = FALSE)

rastrigin20D <- compar(makeRastriginFunction(20), 20, rastriginBounds)
rastrigin20Dms <- rastrigin20D[[1]]
rastrigin20Dprs <- rastrigin20D[[2]]
write.csv(rastrigin20Dms, file = "./data/rastrigin20Dms.csv", row.names = FALSE)
write.csv(rastrigin20Dprs, file = "./data/rastrigin20Dprs.csv", row.names = FALSE)