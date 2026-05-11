# Raport - algorytmy z powracaniem

## Testowanie dla n = 10, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 4
0 2
2 5
3 4
4 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 9
0 4
0 4
0 4
0 4
0 4
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000012 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000110 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000012 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000028 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 9
0 9
1 4
1 7
2 7
3 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 18
0 1
0 1
1 5
1 5
1 5
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000023 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000092 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000050 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000047 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 13
0 6
1 2
1 6
2 4
2 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 27
0 6
0 6
0 6
0 6
0 6
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000089 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000180 | [0, 6, 1, 2, 4, ..., 9, 7, 5, 2, 6]           |
| AHG      | Skierowany - Macierz Grafu         | 0.000128 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000057 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 18
0 3
0 6
0 8
1 2
1 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 36
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000697 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000338 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000030 | [0, 2, 1, 4, 3, ..., 8, 5, 7, 6, 0]           |
| AEG      | Skierowany - Macierz Grafu         | 0.000134 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 22
0 4
0 6
0 8
0 9
1 2
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 45
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000054 | [0, 4, 1, 2, 8, ..., 5, 7, 6, 9, 0]           |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000461 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000137 | [0, 1, 2, 4, 5, ..., 3, 8, 6, 9, 0]           |
| AEG      | Skierowany - Macierz Grafu         | 0.000109 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 27
0 1
0 2
0 3
0 7
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 54
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000435 | [0, 1, 2, 6, 9, ..., 7, 5, 8, 3, 0]           |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000638 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000419 | [0, 1, 2, 7, 4, ..., 5, 6, 8, 9, 0]           |
| AEG      | Skierowany - Macierz Grafu         | 0.000189 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 31
0 2
0 3
0 4
0 6
0 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 62
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000012 | [0, 2, 1, 4, 3, ..., 6, 7, 9, 8, 0]           |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000628 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000020 | [0, 3, 1, 4, 6, ..., 2, 7, 8, 9, 0]           |
| AEG      | Skierowany - Macierz Grafu         | 0.000094 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 36
0 1
0 2
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 72
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000012 | [0, 1, 2, 3, 5, ..., 6, 7, 8, 9, 0]           |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000721 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000026 | [0, 2, 1, 3, 4, ..., 6, 7, 8, 9, 0]           |
| AEG      | Skierowany - Macierz Grafu         | 0.000129 | Acykliczny                                    |
---

## Testowanie dla n = 10, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
10 40
0 1
0 2
0 3
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
10 81
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000015 | [0, 1, 2, 3, 4, ..., 6, 7, 8, 9, 0]           |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000872 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000026 | [0, 1, 2, 3, 4, ..., 6, 7, 9, 8, 0]           |
| AEG      | Skierowany - Macierz Grafu         | 0.000528 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 6
0 7
1 11
2 11
4 6
4 10
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 13
0 4
0 4
0 4
0 4
0 4
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000007 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000109 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000016 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000035 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 13
0 4
0 6
0 10
1 6
1 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 26
0 8
0 8
0 8
0 8
0 8
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000056 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000172 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000039 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000052 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 19
0 5
0 6
0 8
0 9
1 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 39
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000496 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000315 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.001088 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000079 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 26
0 3
0 4
0 9
0 10
0 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 52
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.001070 | [0, 3, 9, 2, 8, ..., 1, 6, 5, 10, 0]          |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000543 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000031 | [0, 3, 2, 5, 6, ..., 10, 9, 11, 1, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000084 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 33
0 4
0 6
0 7
0 8
0 10
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 66
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000029 | [0, 4, 3, 6, 2, ..., 10, 11, 7, 8, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000694 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000016 | [0, 1, 6, 4, 2, ..., 9, 10, 8, 11, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000142 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 39
0 1
0 2
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 79
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000016 | [0, 1, 2, 3, 4, ..., 8, 11, 9, 10, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000727 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000024 | [0, 1, 2, 4, 3, ..., 11, 9, 10, 7, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000229 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 46
0 3
0 4
0 7
0 9
0 10
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 92
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 3, 1, 4, 2, ..., 8, 11, 10, 9, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001034 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000020 | [0, 1, 2, 3, 8, ..., 10, 7, 6, 11, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000232 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 52
0 1
0 2
0 3
0 6
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 105
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000010 | [0, 1, 2, 4, 3, ..., 8, 9, 11, 10, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001194 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000026 | [0, 1, 2, 3, 5, ..., 8, 11, 9, 10, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000249 | Acykliczny                                    |
---

## Testowanie dla n = 12, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
12 59
0 1
0 3
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
12 118
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000009 | [0, 1, 3, 4, 2, ..., 8, 9, 10, 11, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001177 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000021 | [0, 1, 2, 3, 5, ..., 8, 9, 10, 11, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000664 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 9
0 13
1 7
1 8
1 10
2 12
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 18
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000003 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000078 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000005 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000014 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 18
0 3
0 5
0 11
1 3
1 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 36
0 6
0 6
0 6
0 6
0 6
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000249 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000330 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000224 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000056 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 27
0 2
0 3
0 6
0 7
0 10
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 54
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.005542 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000483 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000707 | [0, 1, 4, 7, 6, ..., 11, 13, 8, 3, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000083 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 36
0 1
0 6
0 7
0 10
0 13
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 72
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.001221 | [0, 1, 7, 2, 13, ..., 11, 8, 10, 6, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000483 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000036 | [0, 3, 1, 8, 6, ..., 7, 5, 10, 12, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000129 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 45
0 2
0 3
0 5
0 6
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 91
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000041 | [0, 2, 6, 8, 1, ..., 10, 9, 5, 12, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000622 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000057 | [0, 2, 5, 1, 10, ..., 11, 13, 9, 12, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000360 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 54
0 4
0 5
0 9
1 2
1 3
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 109
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000250 | [0, 4, 2, 1, 3, ..., 11, 7, 13, 9, 0]         |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000991 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000027 | [0, 1, 3, 4, 2, ..., 11, 9, 13, 12, 0]        |
| AEG      | Skierowany - Macierz Grafu         | 0.000213 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 63
0 2
0 3
0 4
0 5
0 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 127
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 2, 1, 3, 5, ..., 9, 12, 13, 11, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001249 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000017 | [0, 2, 1, 3, 4, ..., 12, 11, 10, 13, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000575 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 72
0 1
0 2
0 3
0 6
0 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 145
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000009 | [0, 1, 2, 3, 4, ..., 11, 10, 12, 13, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001338 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000024 | [0, 1, 2, 3, 4, ..., 11, 10, 12, 13, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000187 | Acykliczny                                    |
---

## Testowanie dla n = 14, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
14 81
0 1
0 2
0 3
0 4
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
14 163
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000008 | [0, 1, 2, 3, 4, ..., 10, 11, 12, 13, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001779 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000019 | [0, 1, 2, 3, 4, ..., 10, 11, 12, 13, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000750 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 12
0 8
0 13
1 10
2 4
2 10
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 24
0 5
0 5
0 5
0 5
0 5
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000009 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000094 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000005 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000009 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 24
0 1
0 11
1 4
1 6
1 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 48
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000842 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000361 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000420 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000037 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 36
0 1
0 4
0 5
0 13
1 2
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 72
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.006123 | [0, 1, 3, 13, 5, ..., 8, 12, 10, 4, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000556 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000026 | [0, 2, 4, 8, 1, ..., 14, 15, 9, 7, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000171 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 48
0 3
0 6
0 7
0 13
0 15
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 96
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000265 | [0, 3, 1, 2, 4, ..., 6, 15, 14, 13, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000769 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000019 | [0, 2, 1, 3, 6, ..., 13, 15, 10, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000091 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 60
0 1
0 3
0 10
0 15
1 2
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 120
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000021 | [0, 1, 2, 3, 4, ..., 11, 9, 13, 15, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001106 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000053 | [0, 2, 4, 7, 1, ..., 12, 15, 10, 13, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000243 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 72
0 1
0 6
0 7
0 8
0 12
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 144
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000009 | [0, 1, 3, 5, 2, ..., 9, 13, 15, 14, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001264 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000063 | [0, 2, 8, 1, 3, ..., 15, 12, 10, 11, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000147 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 84
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 168
0 1
0 1
0 1
0 1
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000028 | [0, 1, 2, 3, 4, ..., 10, 12, 13, 15, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001660 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000041 | [0, 1, 2, 4, 3, ..., 12, 15, 11, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000367 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 96
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 192
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000014 | [0, 1, 2, 3, 4, ..., 14, 15, 12, 13, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001911 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000020 | [0, 3, 1, 2, 5, ..., 12, 13, 14, 15, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000158 | Acykliczny                                    |
---

## Testowanie dla n = 16, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
16 108
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
16 216
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000008 | [0, 1, 2, 3, 4, ..., 12, 13, 14, 15, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002150 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000023 | [0, 1, 2, 3, 4, ..., 12, 13, 15, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000972 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 15
0 3
2 3
2 11
2 17
3 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 30
1 7
1 7
1 7
1 7
1 7
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000014 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000118 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000001 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000005 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 30
0 1
0 9
0 10
0 11
0 16
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 61
0 5
0 5
0 5
0 5
0 5
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.003844 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000362 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000328 | [0, 5, 2, 13, 10, ..., 11, 1, 17, 7, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000067 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 45
0 4
0 6
0 10
0 11
0 14
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 91
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 1.440913 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000761 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000042 | [0, 2, 14, 6, 3, ..., 8, 4, 12, 7, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000061 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 61
0 2
0 3
0 5
0 13
0 16
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 122
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000120 | [0, 2, 4, 1, 3, ..., 17, 15, 11, 13, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000969 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000022 | [0, 2, 4, 1, 3, ..., 17, 16, 14, 12, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000219 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 76
0 1
0 3
0 4
0 5
0 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 153
0 4
0 4
0 4
0 4
0 4
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000020 | [0, 1, 2, 4, 5, ..., 12, 16, 9, 17, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001558 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000060 | [0, 4, 1, 2, 8, ..., 10, 11, 15, 17, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000197 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 91
0 1
0 2
0 3
0 5
0 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 183
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000028 | [0, 1, 3, 5, 4, ..., 15, 13, 10, 16, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001868 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000019 | [0, 3, 1, 4, 2, ..., 15, 17, 16, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000627 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 107
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 214
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000026 | [0, 1, 2, 3, 4, ..., 15, 12, 14, 17, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002219 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000020 | [0, 3, 2, 1, 4, ..., 10, 15, 16, 17, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000189 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 122
0 1
0 2
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 244
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000009 | [0, 1, 2, 3, 4, ..., 14, 15, 16, 17, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002643 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000022 | [0, 1, 3, 4, 5, ..., 14, 15, 16, 17, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000995 | Acykliczny                                    |
---

## Testowanie dla n = 18, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
18 137
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
18 275
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000009 | [0, 1, 2, 3, 4, ..., 14, 15, 16, 17, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.003137 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000026 | [0, 1, 2, 4, 3, ..., 14, 15, 17, 16, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001098 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 19
1 12
1 13
1 18
2 15
2 17
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 38
0 9
0 9
0 9
0 9
0 9
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000001 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000084 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000049 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000021 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 38
0 17
0 19
1 5
1 8
1 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 76
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.128833 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000581 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.193819 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000167 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 57
0 1
0 4
0 8
0 11
0 15
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 114
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.023248 | [0, 1, 5, 8, 2, ..., 10, 16, 18, 11, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001125 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000290 | [0, 2, 3, 1, 11, ..., 7, 8, 18, 6, 0]         |
| AEG      | Skierowany - Macierz Grafu         | 0.000067 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 76
0 1
0 4
0 9
0 13
0 15
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 152
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000154 | [0, 1, 2, 7, 5, ..., 16, 13, 17, 18, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001674 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000016 | [0, 2, 4, 1, 3, ..., 18, 16, 19, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000149 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 95
0 1
0 6
0 8
0 12
0 14
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 190
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000338 | [0, 1, 3, 2, 8, ..., 14, 12, 15, 16, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002305 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000052 | [0, 1, 2, 3, 5, ..., 19, 17, 16, 15, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000395 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 114
0 1
0 3
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 228
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000326 | [0, 1, 2, 3, 9, ..., 11, 17, 18, 16, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002765 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000302 | [0, 2, 1, 3, 4, ..., 16, 19, 17, 18, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000259 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 133
0 1
0 2
0 4
0 5
0 7
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 266
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000018 | [0, 1, 2, 3, 5, ..., 19, 16, 18, 17, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.003919 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000038 | [0, 1, 2, 3, 5, ..., 18, 17, 19, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000489 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 152
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 304
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 1, 2, 3, 4, ..., 16, 18, 17, 19, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.004087 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000026 | [0, 1, 2, 3, 4, ..., 17, 16, 18, 19, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001236 | Acykliczny                                    |
---

## Testowanie dla n = 20, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
20 171
0 2
0 5
0 7
0 8
0 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
20 342
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000011 | [0, 2, 1, 3, 5, ..., 16, 17, 18, 19, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.004652 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000029 | [0, 1, 2, 3, 4, ..., 16, 17, 18, 19, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001503 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 23
1 14
2 6
2 16
3 8
3 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 46
0 16
0 16
0 16
0 16
0 16
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000001 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000097 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000003 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000010 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 46
0 8
0 13
0 17
1 2
1 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 92
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 1.021564 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000952 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.001026 | [0, 2, 8, 6, 3, ..., 10, 19, 16, 20, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000088 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 69
0 1
0 3
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 138
0 4
0 4
0 4
0 4
0 4
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.017287 | [0, 1, 7, 3, 4, ..., 20, 11, 16, 5, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001626 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.061107 | [0, 4, 1, 6, 5, ..., 15, 17, 21, 3, 0]        |
| AEG      | Skierowany - Macierz Grafu         | 0.000143 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 92
0 4
0 6
0 7
0 8
0 10
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 184
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000593 | [0, 4, 1, 2, 6, ..., 21, 16, 7, 10, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002541 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000088 | [0, 3, 4, 1, 7, ..., 21, 15, 16, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000253 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 115
0 4
0 8
0 12
0 15
0 16
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 231
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000029 | [0, 4, 1, 3, 2, ..., 18, 19, 11, 17, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.003168 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000038 | [0, 3, 6, 1, 2, ..., 15, 20, 16, 21, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000278 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 138
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 277
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 1, 2, 3, 5, ..., 20, 16, 21, 19, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.004391 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000031 | [0, 1, 3, 4, 2, ..., 20, 21, 18, 17, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000406 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 161
0 1
0 2
0 3
0 5
0 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 323
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 1, 2, 3, 4, ..., 20, 15, 19, 21, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.005387 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000028 | [0, 1, 2, 4, 3, ..., 20, 21, 18, 19, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.002051 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 184
0 2
0 3
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 369
0 1
0 1
0 1
0 1
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 2, 1, 3, 4, ..., 18, 19, 20, 21, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.006142 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000037 | [0, 1, 2, 4, 3, ..., 19, 21, 20, 18, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001327 | Acykliczny                                    |
---

## Testowanie dla n = 22, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
22 207
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
22 415
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000013 | [0, 1, 2, 3, 4, ..., 18, 20, 21, 19, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.006215 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000034 | [0, 1, 2, 3, 4, ..., 18, 19, 20, 21, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.002031 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 27
0 2
0 6
0 9
0 15
0 21
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 55
0 10
0 10
0 10
0 10
0 10
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000351 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000473 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000106 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000042 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 55
0 1
0 2
0 6
0 7
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 110
0 8
0 8
0 8
0 8
0 8
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 3.443398 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000866 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.112265 | [0, 8, 14, 4, 5, ..., 19, 11, 22, 1, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000204 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 82
0 2
0 12
0 20
0 21
1 3
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 165
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.573762 | [0, 2, 4, 3, 1, ..., 19, 20, 18, 21, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.002300 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000145 | [0, 2, 1, 8, 5, ..., 17, 18, 12, 15, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000247 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 110
0 3
0 4
0 5
0 6
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 220
0 2
0 2
0 2
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000020 | [0, 3, 2, 7, 5, ..., 23, 22, 21, 20, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.003525 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000498 | [0, 2, 3, 8, 6, ..., 17, 21, 22, 19, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000781 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 138
0 2
0 3
0 5
0 8
0 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 276
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000019 | [0, 2, 3, 4, 1, ..., 19, 23, 22, 20, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.004338 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000069 | [0, 1, 2, 5, 3, ..., 22, 18, 20, 23, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000625 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 165
0 3
0 4
0 6
0 7
0 9
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 331
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000023 | [0, 3, 1, 2, 4, ..., 23, 22, 21, 20, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.006021 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000038 | [0, 2, 5, 1, 3, ..., 22, 21, 20, 23, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001205 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 193
0 1
0 2
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 386
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000016 | [0, 1, 3, 2, 5, ..., 19, 21, 23, 22, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.007289 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000038 | [0, 1, 3, 2, 6, ..., 20, 21, 23, 22, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000759 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 220
0 1
0 2
0 6
0 7
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 441
0 2
0 2
0 2
0 2
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000015 | [0, 1, 3, 2, 5, ..., 19, 21, 23, 22, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.007972 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000038 | [0, 2, 1, 7, 3, ..., 20, 21, 22, 23, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.003141 | Acykliczny                                    |
---

## Testowanie dla n = 24, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
24 248
0 1
0 3
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
24 496
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000016 | [0, 1, 2, 3, 4, ..., 20, 21, 22, 23, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.009895 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000043 | [0, 1, 2, 3, 4, ..., 19, 21, 22, 23, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.003957 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 32
0 12
0 17
1 12
1 18
2 19
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 65
0 8
0 8
0 8
0 8
0 8
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.003620 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000433 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.003063 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000090 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 65
0 3
0 6
0 9
0 19
0 22
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 130
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.022880 | [0, 3, 1, 6, 4, ..., 19, 15, 14, 22, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001575 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.009062 | [0, 3, 2, 12, 1, ..., 13, 10, 8, 14, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000254 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 97
0 3
0 11
0 13
0 20
0 22
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 195
0 7
0 7
0 7
0 7
0 7
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.004287 | [0, 3, 7, 12, 2, ..., 18, 20, 15, 24, 0]      |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.003477 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.303964 | [0, 7, 12, 1, 2, ..., 20, 18, 24, 9, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000427 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 130
0 1
0 3
0 4
0 11
0 13
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 260
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.004102 | [0, 1, 7, 3, 2, ..., 19, 21, 23, 25, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.004480 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000057 | [0, 1, 3, 2, 8, ..., 23, 22, 25, 18, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000963 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 162
0 1
0 8
0 9
0 10
0 14
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 325
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000216 | [0, 1, 6, 3, 2, ..., 19, 21, 24, 25, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.006071 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000040 | [0, 1, 2, 3, 4, ..., 19, 25, 23, 20, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001269 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 195
0 2
0 6
0 7
0 8
0 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 390
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000151 | [0, 2, 6, 1, 3, ..., 25, 19, 21, 24, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.008183 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000065 | [0, 1, 4, 5, 6, ..., 22, 25, 23, 21, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000666 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 227
0 2
0 3
0 5
0 6
0 8
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 454
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000017 | [0, 2, 1, 3, 4, ..., 21, 23, 24, 25, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.009389 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000064 | [0, 1, 2, 4, 3, ..., 23, 24, 25, 21, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.002468 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 260
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 520
0 3
0 3
0 3
0 3
0 3
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000017 | [0, 1, 2, 4, 3, ..., 22, 23, 24, 25, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.012630 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000044 | [0, 3, 1, 2, 4, ..., 23, 22, 24, 25, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000817 | Acykliczny                                    |
---

## Testowanie dla n = 26, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
26 292
0 1
0 2
0 4
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
26 585
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000016 | [0, 1, 2, 5, 3, ..., 22, 23, 24, 25, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.013378 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000050 | [0, 1, 2, 3, 5, ..., 22, 23, 25, 24, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001692 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 10%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 37
0 13
0 15
0 19
0 25
1 16
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 75
0 15
0 15
0 15
0 15
0 15
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.007275 | Acykliczny                                    |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.000578 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.006465 | Acykliczny                                    |
| AEG      | Skierowany - Macierz Grafu         | 0.000060 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 20%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 75
0 4
0 9
0 15
0 17
0 23
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 151
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 1.106749 | [0, 4, 9, 7, 3, ..., 22, 1, 11, 25, 0]        |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.001766 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.125105 | [0, 1, 19, 3, 4, ..., 9, 14, 26, 10, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000368 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 30%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 113
0 2
0 3
0 9
0 10
0 15
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 226
0 6
0 6
0 6
0 6
0 6
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.068278 | [0, 2, 5, 1, 7, ..., 21, 17, 25, 23, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.004145 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.001536 | [0, 6, 1, 4, 2, ..., 24, 11, 16, 21, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000978 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 40%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 151
0 4
0 7
0 8
0 10
0 12
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 302
0 6
0 6
0 6
0 6
0 6
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000036 | [0, 4, 6, 1, 5, ..., 27, 24, 25, 26, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.006366 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000055 | [0, 6, 4, 7, 3, ..., 20, 22, 25, 26, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000817 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 50%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 189
0 1
0 9
0 10
0 11
0 14
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 378
0 1
0 1
0 1
0 1
0 1
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000018 | [0, 1, 3, 4, 5, ..., 23, 25, 26, 27, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.008259 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000037 | [0, 1, 2, 3, 4, ..., 23, 26, 24, 27, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000858 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 60%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 226
0 1
0 2
0 5
0 7
0 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 453
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000019 | [0, 1, 3, 7, 2, ..., 25, 26, 24, 27, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.010851 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000053 | [0, 1, 4, 2, 5, ..., 27, 25, 24, 26, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001880 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 70%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 264
0 1
0 2
0 3
0 4
0 11
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 529
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000019 | [0, 1, 3, 2, 4, ..., 24, 25, 26, 27, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.014372 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000045 | [0, 1, 2, 5, 3, ..., 24, 25, 26, 27, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.001951 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 80%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 302
0 1
0 2
0 3
0 4
0 5
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 604
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000019 | [0, 1, 2, 3, 4, ..., 25, 23, 26, 27, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.015489 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000051 | [0, 1, 2, 3, 4, ..., 24, 25, 26, 27, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.004880 | Acykliczny                                    |
---

## Testowanie dla n = 28, nasycenie = 90%
### Parametry wejściowe (fragment pliku - graf nieskierowany):
```text
28 340
0 1
0 2
0 3
0 5
0 6
...
```
### Parametry wejściowe (fragment pliku - multigraf skierowany):
```text
28 680
0 1
0 1
0 1
0 2
0 2
...
```

### Wyniki wyszukiwania cykli:
| Algorytm | Reprezentacja                      | Czas [s] | Wynik (fragment)                              |
|:--------|:----------------------------------|:--------|:---------------------------------------------|
| AHS      | Nieskierowany - Macierz Sąsiedztwa | 0.000021 | [0, 1, 2, 3, 4, ..., 24, 25, 27, 26, 0]       |
| AES      | Nieskierowany - Macierz Sąsiedztwa | 0.016735 | Acykliczny                                    |
| AHG      | Skierowany - Macierz Grafu         | 0.000056 | [0, 1, 2, 4, 3, ..., 22, 25, 26, 27, 0]       |
| AEG      | Skierowany - Macierz Grafu         | 0.000902 | Acykliczny                                    |
---

# Wykresy
![AHS - nieskierowane](/Plots/AHS_nieskierowane.png)
![AES - nieskierowane](/Plots/AES_nieskierowane.png)
![AHG - skierowane](/Plots/AHG_skierowane.png)
![AEG - skierowane](/Plots/AEG_skierowane.png)

# Wnioski

### 1. Klasy złożoności i złożoność algorytmów

| Problem       | Klasa - Wersja Decyzyjna                                    | Klasa - Wersja Poszukiwania                            | Złożoność wdrożonego algorytmu                                                                                  | Czy Cykl i Ścieżka to ta sama klasa?                                                     |
|:--------------|:------------------------------------------------------------|:-------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| **Hamiltona** | **NP-zupełna**                                              | **NP-trudna**                                          | **O(V!)** (Robertsa-Floresa) - pesymistyczny czas rośnie silniowo ze względu na sprawdzanie wszystkich ścieżek. | **Tak**. Zarówno cykl jak i ścieżka Hamiltona są problemami NP-zupełnymi / NP-trudnymi.  |
| **Eulera**    | **P** (wystarczy O(V+E) na sprawdzenie stopni wierzchołków) | **P** (problem można rozwiązać w czasie wielomianowym) | **O(E²)** (Fleury'ego) - w każdym kroku sprawdzamy mosty (złożoność rzędu O(E)), E = liczba krawędzi.           | **Tak**. Zarówno cykl jak i ścieżka Eulera należą do klasy problemów wielomianowych (P). |

<br>

### 2. Obserwacje z działania algorytmów

| Aspekt testów                        | Krótkie wnioski i obserwacje                                                                                                                                                                                                                                          |
|:-------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Wpływ liczby wierzchołków (n)**    | Czas działania algorytmów Hamiltona (AHS, AHG) rośnie drastycznie i wykładniczo wraz ze wzrostem $n$. Dla problemów Eulera (AES, AEG) algorytm radzi sobie w ułamkach sekund, niezależnie od wielkości badanej próbki.                                                |
| **Wpływ nasycenia (Hamilton)**       | Bardzo wysokie nasycenie sprawia, że algorytm szybko na cykl. Najgorzej jest w grafach gęstych, w których **nie ma cyklu** – algorytm musi wtedy powracać (backtracking) tysiące razy, co drastycznie wydłuża czas.                                                   |
| **Wpływ nasycenia (Euler)**          | Im wyższe nasycenie, tym dłuższy czas działania algorytmu. Wzrost czasu jest jednak jednostajny.                                                                                                                                                                      |
| **Grafy Skierowane a Nieskierowane** | W multigrafach skierowanych ruch dozwolony jest tylko w jednym kierunku. Oznacza to mniej "ślepych uliczek" do sprawdzenia w przypadku braku cyklu, przez co czas weryfikacji grafu acyklicznego przez algorytm AHG potrafi być mniejszy niż dla nieskierowanego AHS. |
