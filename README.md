# Algorytm Needlemana-Wunscha (globalne dopasowanie sekwencji)

## Opis programu
Program wykonuje globalne dopasowanie dwóch sekwencji aminokwasowych za pomocą algorytmu Needlemana-Wunscha.

## Uruchomienie programu

Do uruchomienia programu potrzebne są:
- Python 3,
- biblioteka NumPy.

Program należy uruchomić z trzema argumentami:
1. Nazwą pierwszego pliku wejściowego w formacie FASTA,
2. Nazwą drugiego pliku wejściowego w formacie FASTA,
3. Wybraną nazwą pliku wynikowego.

Przykład uruchomienia:
```bash
python3 needleman_wunsch.py sekwencja1.fasta sekwencja2.fasta wynik.txt
```

Po uruchomieniu program wyświetli:
```text
Macierz przeliczona (wymiary: 12x11).
Wynik zapisano w pliku: wynik.txt
```

## Punktacja

W programie zastosowano następującą punktację:
- match (zgodność aminokwasów): +1
- mismatch (niezgodność aminokwasów): -1
- gap (przerwa): -2
  
## Przykładowy plik wynikowy

Dla plików:
- sekwencja1.fasta - MKTAYIAKQRQ
- sekwencja2.fasta - MKTAFIAKRQ

Plik wynikowy powinien wyglądać następująco:

```text
Globalne dopasowanie Needlemana-Wunscha
Score: 6.0
MKTAYIAKQRQ
|||| ||| ||
MKTAFIAK-RQ
```

Znak `|` oznacza dopasowanie, a znak `-` oznacza wprowadzenie przerwy.
