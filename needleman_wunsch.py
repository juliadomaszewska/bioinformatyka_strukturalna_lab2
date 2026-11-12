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

    Sciezka = np.zeros((dlugosc1 + 1, dlugosc2 + 1))