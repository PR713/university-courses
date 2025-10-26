from scipy.optimize import newton, brentq

#a- to jest f(x) = x^3 - 5x, x0=1
#miedzy x=-1 a x=1 bo f'(1) = f'(-1)
#występuje cykl dwupunktowy nigdy nie przerwany
def f_a(x):
    return x**3 - 5*x

#pochodna
def f_a_prime(x):
    return 3*x**2 - 5

print("Part (a)")
#try Newton
#zawsze powinien zadziałać catch
try:
    root_a = newton(f_a, 1, fprime=f_a_prime, maxiter=10)
    print("  Newton zbiega do:", root_a)
except Exception as e:
    print("  Newton nie zadzialał:", e)

# Bracketing (brentq) to find all real roots
roots_a = [brentq(f_a, -3, -1), brentq(f_a, -1, 1), brentq(f_a, 1, 3)]      #pierwiastki na przedziałach <-3,-1>, <-1,1>, <1,3>
print("  brentq pierwiastki:", roots_a)


# f(x) = x^3 - 3x + 1, x0 = 1
#f'(1) = 0- dzielenie przez 0
def f_b(x):
    return x**3 - 3*x + 1

def f_b_prime(x):
    return 3*x**2 - 3

print("\nPart (b)")
#try Newton
try:
    root_b = newton(f_b, 1, fprime=f_b_prime, maxiter=10)
    print("  Newton zbiega do:", root_b)
except Exception as e:
    print("  Newton nie zadzialał:", e)

# Secant- zamiast 1 wartości startowej dwie-wzór bez pochodnej lub brentq
root_b_secant = newton(f_b, 1, x1=2, tol=1e-8, maxiter=50)
print("  Secant newton zbiega do:", root_b_secant)
roots_b = [brentq(f_b, -2, 0), brentq(f_b, 0, 1), brentq(f_b, 1, 2)]
print("  brentq pierwiastki:", roots_b)


# Part (c): f(x) = 2 - x^5, x0 = 0.01
#W otoczeniu x=0 pochodna zbiega do 0 więc Newton robi bardzo duże kroki
def f_c(x):
    return 2 - x**5

def f_c_prime(x):
    return -5*x**4

print("\nPart (c)")
#try Newton
try:
    root_c = newton(f_c, 0.01, fprime=f_c_prime, tol=1e-8)
    print("  Newton zbiega do:", root_c)
except Exception as e:
    print("  Newton nie zadzialał:", e)

# Secant lub brentq
root_c_secant = newton(f_c, 0.5, x1=1.5, tol=1e-8)
print("  Secant newton zbiega do:", root_c_secant)
root_c_brent = brentq(f_c, 0, 2)
print("  brentq pierwiastek:", root_c_brent)


#f(x) = x^4 - 4.29 x^2 - 5.29, x0 = 0.8
#Oscylacja, raz ujemne wartości, raz dodatnie więc skaczemy między dwoma wartościami, zastosowanie secant nie pomaga
def f_d(x):
    return x**4 - 4.29*x**2 - 5.29

def f_d_prime(x):
    return 4*x**3 - 8.58*x

print("\nPart (d)")

#try newton zwykły
try:
    root_d_newton = newton(f_d, 0.8, fprime=f_d_prime, tol=1e-8, maxiter=50)
    print("  Newton z pochodną zbiega do:", root_d_newton)
except Exception as e:
    print("  Newton z pochodną nie zadzialał:", e)

#try newton secant(żeby nie było pochodnej)
try:
    root_d_secant = newton(f_d, 0.8, tol=1e-8, maxiter=50)
    print("  Secant (bez pochodnej) zbiega do:", root_d_secant)
except Exception as e:
    print("  Secant nie zadzialał:", e)

#Znajdujemy rzeczywiste pierwiastki przez brentq
root_d_pos = brentq(f_d, 1, 3)
root_d_neg = brentq(f_d, -3, -1)
print("  brentq pierwiastki:", root_d_neg, root_d_pos)
