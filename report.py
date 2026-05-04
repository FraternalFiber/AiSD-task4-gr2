import numpy as np
import matplotlib.pyplot as plt


def print_markdown_report(raw_data_report):
    print("\n" + "=" * 50)
    print(" RAPORT KOŃCOWY (MARKDOWN) ")
    print("=" * 50 + "\n")

    print("# Raport z wykonania algorytmów z powracaniem\n")

    print("## 1. Wyniki testów (Dane wejściowe i czasy wykonania)\n")
    print(
        "| Typ Grafu | Liczba wierzchołków (n) | Nasycenie (s%) | Wynik Hamilton | Czas Hamilton (s) | Wynik Euler | Czas Euler (s) |")
    print(
        "|-----------|-------------------------|----------------|----------------|-------------------|-------------|----------------|")

    for row in raw_data_report:
        g_type, n, s, t_ham, res_ham, t_eul, res_eul = row
        print(f"| {g_type} | {n} | {s}% | {res_ham} | {t_ham:.6f} | {res_eul} | {t_eul:.6f} |")

    print("\n## 2. Złożoność obliczeniowa i klasy problemów\n")
    print("### Złożoność algorytmów zaimplementowanych w projekcie:")
    print(
        "- **AHS / AHG (Algorytm Robertsa-Floresa dla cyklu Hamiltona):** Algorytm opiera się na technice przeszukiwania z nawrotami (backtracking). Pesymistyczna złożoność czasowa wynosi **O(V!)**, ponieważ w najgorszym przypadku algorytm może sprawdzić każdą możliwą permutację wierzchołków.")
    print(
        "- **AES / AEG (Algorytm Fleury'ego dla cyklu Eulera):** Algorytm w każdym kroku wyszukuje krawędzi, omijając mosty. Samo sprawdzanie mostów (przez DFS/BFS) zajmuje O(E). Zatem całkowita złożoność czasowa to **O(E^2)**.\n")

    print("### Klasy złożoności obliczeniowej:")
    print("- **Problem cyklu Hamiltona (wersja decyzyjna):** Należy do klasy **NP-zupełnych (NP-Complete)**.")
    print("- **Problem cyklu Hamiltona (wersja poszukiwania):** Należy do klasy **NP-trudnych (NP-Hard)**.")
    print(
        "- **Problem cyklu Eulera (wersja decyzyjna):** Należy do klasy **P** (wystarczy sprawdzić parzystość stopni wierzchołków w czasie O(V+E)).")
    print("- **Problem cyklu Eulera (wersja poszukiwania):** Należy do klasy **P**.\n")

    print("### Cykl a ścieżka:")
    print(
        "Problemy poszukiwania **ścieżki Hamiltona** i **cyklu Hamiltona** należą do tej samej klasy złożoności (oba są NP-trudne). Podobnie w przypadku **ścieżki Eulera** i **cyklu Eulera** – oba problemy rozwiązuje się w czasie wielomianowym (klasa P).\n")

    print("## 3. Obserwacje\n")
    print(
        "- Zgodnie z przewidywaniami, czas działania algorytmów poszukujących cyklu Hamiltona rośnie drastycznie (silniowo) wraz ze wzrostem liczby wierzchołków `n`.")
    print(
        "- Algorytm Fleury'ego, choć posiada zauważalną narzutę wynikającą ze sprawdzania mostów w każdej iteracji, wykonuje się w ułamku sekundy dla testowanych zakresów `n` i `s`, co dobitnie obrazuje różnicę pomiędzy problemami klasy P i NP.")
    print(
        "- Różne nasycenie grafu różnie wpływa na czas: dla Hamiltona w bardzo gęstych grafach cykl (jeśli istnieje) jest szybko znajdowany dzięki licznym rozgałęzieniom, lecz w przypadku braku cyklu, czas weryfikacji wszystkich gałęzi drastycznie rośnie.\n")


def plot_3d_surfaces(results):
    fig = plt.figure(figsize=(12, 10))
    titles = ['AHS (Hamilton - Nieskierowane)', 'AES (Euler - Nieskierowane)',
              'AHG (Hamilton - Skierowane)', 'AEG (Euler - Skierowane)']
    keys = ['AHS', 'AES', 'AHG', 'AEG']

    for i, key in enumerate(keys):
        ax = fig.add_subplot(2, 2, i + 1, projection='3d')

        n_vals = np.array(results[key]['n'])
        s_vals = np.array(results[key]['s'])
        t_vals = np.array(results[key]['time'])

        # Konwersja list punktów do siatki 2D dla matplolib
        N_unique = sorted(list(set(n_vals)))
        S_unique = sorted(list(set(s_vals)))
        N, S = np.meshgrid(N_unique, S_unique)
        T = np.zeros_like(N, dtype=float)

        for n_v, s_v, t_v in zip(n_vals, s_vals, t_vals):
            # Znajdź odpowiednie indeksy w macierzy meshgrid
            r = S_unique.index(s_v)
            c = N_unique.index(n_v)
            T[r, c] = t_v

        surf = ax.plot_surface(N, S, T, cmap='viridis', edgecolor='none')
        ax.set_title(titles[i])
        ax.set_xlabel('Liczba wierzchołków (n)')
        ax.set_ylabel('Nasycenie (%)')
        ax.set_zlabel('Czas [s]')
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()