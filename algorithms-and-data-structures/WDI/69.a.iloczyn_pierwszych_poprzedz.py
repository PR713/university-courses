def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0: return False
        return True
    else:
        return False


def zad(T):
    n = len(T)
    maxi = 1
    ind = 0
    i = 0
    final = 0
    ilo_prev = 1
    ilo = 1
    while i < n:
        for j in range(ind, i):
            if is_prime(T[j]):
                ilo_prev = ilo
                ilo *= T[j]
            if T[i] == ilo:
                if T[i] > ilo_prev:
                    ilo_prev = ilo
                    final = i
        ind = i #na bieżąco doliczamy następne do iloczynu a nie wszystkie od początku
        i += 1
    return final if final != 0 else None


T = [2, 4, 5, 7, 70, 7, 2, 980, 100]
print(zad(T))
