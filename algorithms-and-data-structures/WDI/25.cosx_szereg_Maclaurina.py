x = float(input('Podaj wartość x dla której obliczyć cosx: '))

silnia_parzysta = 1
licznik_ulamkow = 2
potega_licznika_ulamka = 0
ulamek = 1 #tylko żeby wejść do while'a
ulamek_poprzedni = 0
i = 2
eps = 1e-10
cosx = 1

while abs(ulamek_poprzedni-ulamek) > eps:
    silnia_parzysta *= i
    i += 1
    if (i-1) % 2 == 0:
       potega_licznika_ulamka += 2
       ulamek_poprzedni = ulamek
       if licznik_ulamkow % 2 == 0:
          ulamek = (-1) * x **(potega_licznika_ulamka) / silnia_parzysta
          cosx += ulamek
          licznik_ulamkow += 1
       else:
          ulamek = x **(potega_licznika_ulamka) / silnia_parzysta
          cosx += ulamek
          licznik_ulamkow += 1
print(f'Wartośc cos dla x = {x} wynosi: {cosx}')