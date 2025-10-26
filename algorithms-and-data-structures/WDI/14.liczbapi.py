from math import sqrt

n = 0.5
iloczyn = 1
pierwiastek = sqrt(n)

for i in range(50):
    iloczyn *= pierwiastek
    pierwiastek = sqrt(0.5 +0.5*pierwiastek)
# print(iloczyn) # 2 przez pi
print(f'Liczba π wynosi : {2 / iloczyn}')

quit('<3 <3 <3')
