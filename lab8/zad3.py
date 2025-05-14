import mpmath as mp

#ustalamy precyzję obliczeń(to jest liczba cyfr po przecinku)
mp.mp.dps = 80

#definicje funkcji i ich pochodnych dla podpunktów (a), (b), (c)
eqs = [
    ('a', lambda x: x**3 - 2*x - 5,         lambda x: 3*x**2 - 2,            2),  #zgadujemy pierwiastek ok. 2
    ('b', lambda x: mp.e**(-x) - x,         lambda x: -mp.e**(-x) - 1,       0),  #zgadujemy pierwiastek ok. 0
    ('c', lambda x: x*mp.sin(x) - 1,        lambda x: mp.sin(x) + x*mp.cos(x), 1)   #zgadujemy pierwiastek ok. 1
]

#funkcja obliczająca liczbę iteracji Newtona potrzebnych do osiągnięcia zadanej liczby bitów precyzji

def iters_for_precision(f, fprime, x_ref, x0, target_bits):
    x = x0
    for k in range(1, 50):  # ograniczamy do 50 iteracji
        # wykonujemy jedną iterację Newtona
        x = x - f(x)/fprime(x)
        # błąd bezwzględny
        e = abs(x - x_ref)
        # liczba bitów dokładności (przybliżenie floor)
        bits = mp.floor(-mp.log(e, 2))
        if bits >= target_bits:
            return k, bits
    return None, bits

#początkowa liczba bitów (przybliżenie ma 4 bity dokładności)
initial_bits = 4

# Dla każdego równania: obliczamy iteracje dla 24- i 53-bitowej dokładności
for name, f, fprime, guess in eqs:
    #wyznaczamy pierwiastek referencyjny z dużą precyzją
    x_ref = mp.findroot(f, guess)
    #tworzymy przybliżenie początkowe x0 o 4-bitowej dokładności: dodajemy błąd 2^(-4)
    x0 = x_ref + mp.mpf(2)**(-initial_bits)

    print(f"Podpunkt ({name}):")
    print(f"  Pierwiastek referencyjny: {x_ref}")
    print(f"  Początkowe x0: {x0} (ok. {initial_bits} bitów)")

    for target in [24, 53]:
        k, achieved = iters_for_precision(f, fprime, x_ref, x0, target)
        print(f"  Aby osiągnąć >= {target} bitów: iteracji = {k}, uzyskano {achieved} bitów")
    print()
