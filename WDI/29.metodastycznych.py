# METODA STYCZNYCH to metoda Newtona jako sqrt x stopnia z 2020
# x^x = 2020 -> x^x - 2020 = 0
from math import log,e
def f(x):
    return x**x - 2020

def f_prime(x):
    return (x**x) * (log(x,e)+1)

def Newton(x0, eps = 1e-6):
    while abs(f(x0)) > eps:
        x0 = x0 - f(x0)/f_prime(x0)
    return x0, f(x0)+2020

#dowolna np 4
print(Newton(4))