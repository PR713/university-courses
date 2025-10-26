#dla trójwymiaru po prostu prefix x,y,z
#np count_xy[][] to tablica dwuwymiarowa wypełniana w O(n^2)
# n = x + y + z - xy - xz - zy + xyz + P, P = 1 maksymalna dominacja
# s = n - x - y - z + xy + xz + xy - 1
#a potem prefix_xy[][] zliczana w n^2,
#for x,y,_ in P:
#    xy_count[x][y] += 1
#for i in range(1, n + 1):
#    for j in range(1, n + 1):
#       prefix_xy_sum[i][j] = prefix_xy_sum[i - 1][j] +\
#       prefix_xy_sum[i][j - 1] - prefix_xy_sum[i - 1][j - 1] + xy_count[i][j]
#czyli wyżej do lewego rogu + w lewo do lewego rogu - [i-1][j-1] część wspólna
#liczona dwa razy, na [i][j] współrzędne x <= i, y <= j
#max s to maksymalna siła znaleziona
#dodaliśmy 3 razy sześcian i 3 razy odjęliśmy więc szukamy ile
#jest w sześcianie xyz = s, można razem ze znalezieniem indeksów zawsze