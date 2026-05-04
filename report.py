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
    """ Wyświetla każdy wykres w osobnym oknie z poprawionym formatowaniem """
    titles = {
        'AHS': 'AHS (Hamilton - Macierz Sąsiedztwa)',
        'AES': 'AES (Euler - Macierz Sąsiedztwa)',
        'AHG': 'AHG (Hamilton - Macierz Grafu)',
        'AEG': 'AEG (Euler - Macierz Grafu)'
    }

    for key in ['AHS', 'AES', 'AHG', 'AEG']:
        if not results[key]['n']: continue

        # Tworzenie nowego okna dla każdego algorytmu
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        n_vals = np.array(results[key]['n'])
        s_vals = np.array(results[key]['s'])
        t_vals = np.array(results[key]['time'])

        # Przygotowanie siatki danych (Grid)
        N_unique = sorted(list(set(n_vals)))
        S_unique = sorted(list(set(s_vals)))
        N_grid, S_grid = np.meshgrid(N_unique, S_unique)
        T_grid = np.zeros_like(N_grid, dtype=float)

        for n_v, s_v, t_v in zip(n_vals, s_vals, t_vals):
            r = S_unique.index(s_v)
            c = N_unique.index(n_v)
            T_grid[r, c] = t_v

        # Rysowanie powierzchni
        surf = ax.plot_surface(N_grid, S_grid, T_grid, cmap='turbo', edgecolor='none', alpha=0.9)

        # Konfiguracja tytułu i etykiet
        ax.set_title(titles[key], pad=20, fontsize=14, fontweight='bold')

        # Kluczowe: labelpad odsuwa opis osi od skali (liczb), zapobiegając nachodzeniu
        ax.set_xlabel('Liczba wierzchołków (n)', labelpad=15)
        ax.set_ylabel('Nasycenie (%)', labelpad=15)
        ax.set_zlabel('Czas wykonania [s]', labelpad=15)

        # Opcjonalnie: dostosowanie kąta widzenia dla lepszej czytelności
        ax.view_init(elev=25, azim=-45)

        # Pasek koloru
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.1)

        plt.tight_layout()
        # Nie dajemy plt.show() tutaj, bo zablokuje pętlę

    # Wyświetlamy wszystkie okna na raz na samym końcu
    plt.show()