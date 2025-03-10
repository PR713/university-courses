import numpy as np
import matplotlib.pyplot as plt
import math

def kahan_sum(x):
    suma = np.float32(0.0)
    komp = np.float32(0.0)
    for xi in x:
        y = np.float32(xi - komp)
        temp = np.float32(suma + y)
        komp = np.float32((temp - suma) - y)
        suma = temp
    return suma


n_values = [10 ** k for k in range(4, 9)]

errors_a = []
errors_b = []
errors_c = []
errors_d = []
errors_e = []

for n in n_values:
    x = np.random.uniform(0, 1, n).astype(np.float32)
    true_sum = math.fsum(x.tolist())

    sum_a = np.cumsum(x, dtype=np.float64)[-1]

    sum_b = np.cumsum(x, dtype=np.float32)[-1]

    sum_c = kahan_sum(x)

    x_sorted_asc = np.sort(x)
    sum_d = np.cumsum(x_sorted_asc, dtype=np.float32)[-1]

    x_sorted_desc = np.sort(x)[::-1]
    sum_e = np.cumsum(x_sorted_desc, dtype=np.float32)[-1]

    err_a = abs(sum_a - true_sum) / abs(true_sum)
    err_b = abs(sum_b - true_sum) / abs(true_sum)
    err_c = abs(sum_c - true_sum) / abs(true_sum)
    err_d = abs(sum_d - true_sum) / abs(true_sum)
    err_e = abs(sum_e - true_sum) / abs(true_sum)

    errors_a.append(err_a)
    errors_b.append(err_b)
    errors_c.append(err_c)
    errors_d.append(err_d)
    errors_e.append(err_e)

    print(f"n = {n:>10}:")
    print(f"  (a) podwójna precyzja: suma = {sum_a:.8e}, błąd = {err_a:.8e}")
    print(f"  (b) pojedyncza precyzja: suma = {sum_b:.8e}, błąd = {err_b:.8e}")
    print(f"  (c) Kahan:             suma = {sum_c:.8e}, błąd = {err_c:.8e}")
    print(f"  (d) sort. rosnąco:     suma = {sum_d:.8e}, błąd = {err_d:.8e}")
    print(f"  (e) sort. malejąco:    suma = {sum_e:.8e}, błąd = {err_e:.8e}")
    print()

plt.figure(figsize=(10, 6))
plt.loglog(n_values, errors_a, 'o-', label='(a) Akumulacja double')
plt.loglog(n_values, errors_b, 's-', label='(b) Akumulacja float')
plt.loglog(n_values, errors_c, '^-', label='(c) Kahan')
plt.loglog(n_values, errors_d, 'd-', label='(d) Sort. rosnąco')
plt.loglog(n_values, errors_e, 'v-', label='(e) Sort. malejąco')
plt.xlabel('Liczba elementów n')
plt.ylabel('Względny błąd')
plt.title('Względny błąd sumowania w zależności od n')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()