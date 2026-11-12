import sys
import numpy as np

SKOS = 1
GORA = 2
LEWO = 3

def main():
    nazwa_plik1 = sys.argv[1]
    nazwa_plik2 = sys.argv[2]
    nazwa_plik_wynik = sys.argv[3]

    try:
        with open(nazwa_plik1, "r") as plik1:
            next(plik1)
            sekwencja1 = plik1.read().replace('\n', '').strip()

        with open(nazwa_plik2, "r") as plik2:
            next(plik2)
            sekwencja2 = plik2.read().replace('\n', '').strip()

    except PlikNieznaleziony:
          print("Blad wczytywania pliku")
          sys.exit(1)

    dlugosc1=len(sekwencja1)
    dlugosc2=len(sekwencja2)
    gap_penalty = -2

    Macierz = np.zeros((dlugosc1 + 1, dlugosc2 + 1))

    Sciezka = np.zeros((dlugosc1 + 1, dlugosc2 + 1), dtype = int)

    for i in range(dlugosc1 + 1):
        Macierz[i][0] = gap_penalty * i
        Sciezka[i][0] = GORA

    for j in range(dlugosc2 + 1):
        Macierz[0][j] = gap_penalty * j
        Sciezka[0][j] = LEWO

    for i in range (1, dlugosc1 +1):
        for j in range (1, dlugosc2 + 1):
            match = Macierz[i-1][j-1] + (1 if sekwencja1[i-1] == sekwencja2[j-1] else -1)
            delete = Macierz[i-1][j] + gap_penalty
            insert = Macierz[i][j-1] + gap_penalty
            Macierz[i][j] max(match, delete, insert)

            if Macierz[i][j] == match:
                Sciezka[i][j] = SKOS
            elif Macierz[i][j] == delete:
                Sciezka[i][j] = GORA
            else:
                Sciezka[i][j] = LEWO

    i, j = dlugosc1, dlugosc2
    dopasowana_sekwencja1 = ""
    dopasowana_sekwencja2 = ""

    while i > 0 and j > 0:
        if Sciezka [i][j] == SKOS:
            dopasowana_sekwencja1 = sekwencja1[i-1] + dopasowana_sekwencja1
            dopasowana_sekwencja2 = sekwencja2[j-1] + dopasowana_sekwencja2
            i -= 1
            j -= 1
        elif Sciezka [i][j] == GORA:
            dopasowana_sekwencja1 = sekwencja1[i-1] + dopasowana_sekwencja1
            dopasowana_sekwencja2 = "-" + dopasowana_sekwencja2
            i -= 1
        else:
            dopasowana_sekwencja1 = "-" +  dopasowana_sekwencja1
            dopasowana_sekwencja2 = sekwencja2[j-1] + dopasowana_sekwencja2
            j -= 1

    while i>0:
        dopasowana_sekwencja1 = sekwencja1[i-1] + dopasowana_sekwencja1
        dopasowana_sekwencja2 = "-" + dopasowana_sekwencja2
        i -= 1

    while j>0:
        dopasowana_sekwencja1 = "-" + dopasowana_sekwencja1
        dopasowana_sekwencja2 = dopasowana_sekwencja2[j-1] + dopasowana_sekwencja2
        j -= 1

    linia_dopasowania = "".join(["|" if a == b else " " for a, b in zip(dopasowana_sekwencja1, dopasowana_sekwencja2)])

    with open (nazwa_plik_wynik, "w") as plik:
        plik.write ("Globlne dopasowanie Needlemana-Wunscha\n")
        plik.write ("Score: "+ str(Macierz[dlugosc1][dlugosc2])+ "\n")
        plik.write(dopasowana_sekwencja1 + "\n")
        plik.write(linia_dopasowania + "\n")
        plik.write(dopasowana_sekwencja2 + "\n")

    print(f"Macierz przeliczona (wymiary: {dlugosc1+1}x{dlugosc2+1}).")
    print(f"Wynik zapisano w pliku: {nazwa_plik_wynik}")

main()