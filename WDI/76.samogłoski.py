def czy_samogloska(ch):
    samogloski = ['a', 'e', 'y', 'i', 'o', 'u']
    return 1 if ch in samogloski else 0

def wyraz(s1, s2):
    samogloski_s1 = 0
    suma_ascii_s1 = 0
    n = len(s2)
    for i in range(len(s1)):
        samogloski_s1 += czy_samogloska(s1[i])
        suma_ascii_s1 += ord(s1[i])

    # indeks, suma wartosci w tabeli ascii, cnt - ilosc samoglosek
    def rek(i, suma_ascii, cnt):
        if i == n:
            return suma_ascii == suma_ascii_s1 and cnt == samogloski_s1

        return rek(i + 1, suma_ascii, cnt) or rek(i + 1, suma_ascii + ord(s2[i]), cnt + czy_samogloska(s2[i]))

    return rek(0, 0, 0)