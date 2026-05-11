import numpy as np
import matplotlib.pyplot as plt


def format_path(path):
    """
    Formatowanie wyniku.
    """
    if path is None:
        return "Acykliczny"

    if len(path) <= 10:
        return str(path)

    # Dla list dłuższych niż 10 elementów: bierzemy 5 pierwszych i 5 ostatnich
    start = ", ".join(map(str, path[:5]))
    end = ", ".join(map(str, path[-5:]))
    return f"[{start}, ..., {end}]"


def print_live_markdown_block(n, s, e_undir, edges_sample_undir, e_dir, edges_sample_dir, res_ahs, t_ahs, res_aes,
                              t_aes, res_ahg, t_ahg, res_aeg, t_aeg):
    """ Wypisuje na bieżąco wyniki testu z parametrami (wycinek pliku) i tabelą """

    print(f"\n## Testowanie dla n = {n}, nasycenie = {s}%")

    # Fragment pliku dla grafu nieskierowanego
    print("### Parametry wejściowe (fragment pliku - graf nieskierowany):")
    print("```text")
    print(f"{n} {e_undir}")
    for edge in edges_sample_undir:
        print(edge)
    print("...")
    print("```")

    # Fragment pliku dla grafu skierowanego
    print("### Parametry wejściowe (fragment pliku - multigraf skierowany):")
    print("```text")
    print(f"{n} {e_dir}")
    for edge in edges_sample_dir:
        print(edge)
    print("...")
    print("```\n")

    # Tabela z wynikami (z odpowiednim formatowaniem Markdown)
    print("### Wyniki wyszukiwania cykli:")
    print(f"| {'Algorytm':<8} | {'Reprezentacja':<34} | {'Czas [s]':<8} | {'Wynik (fragment)':<45} |")
    print(f"|:{'-' * 8}|:{'-' * 34}|:{'-' * 8}|:{'-' * 45}|")

    def print_row(algo, rep, t, path):
        t_str = f"{t:.6f}"
        path_str = format_path(path)
        print(f"| {algo:<8} | {rep:<34} | {t_str:<8} | {path_str:<45} |")

    print_row("AHS", "Nieskierowany - Macierz Sąsiedztwa", t_ahs, res_ahs)
    print_row("AES", "Nieskierowany - Macierz Sąsiedztwa", t_aes, res_aes)
    print_row("AHG", "Skierowany - Macierz Grafu", t_ahg, res_ahg)
    print_row("AEG", "Skierowany - Macierz Grafu", t_aeg, res_aeg)
    print("---")


def plot_3d_surfaces(results):
    """ Tworzy 4 osobne okna z wykresami 3D """
    titles = {
        'AHS': 'AHS (Hamilton - Nieskierowane)',
        'AES': 'AES (Euler - Nieskierowane)',
        'AHG': 'AHG (Hamilton - Skierowane)',
        'AEG': 'AEG (Euler - Skierowane)'
    }

    for key, title in titles.items():
        # Tworzenie nowego okna dla każdego wykresu
        fig = plt.figure(figsize=(10, 8))

        # Opcjonalne: Ustawienie tytułu samego okna systemowego
        fig.canvas.manager.set_window_title(title)

        ax = fig.add_subplot(111, projection='3d')

        n_vals = np.array(results[key]['n'])
        s_vals = np.array(results[key]['s'])
        t_vals = np.array(results[key]['time'])

        N_unique = sorted(list(set(n_vals)))
        S_unique = sorted(list(set(s_vals)))
        N, S = np.meshgrid(N_unique, S_unique)
        T = np.zeros_like(N, dtype=float)

        for n_v, s_v, t_v in zip(n_vals, s_vals, t_vals):
            r = S_unique.index(s_v)
            c = N_unique.index(n_v)
            T[r, c] = t_v

        surf = ax.plot_surface(N, S, T, cmap='viridis', edgecolor='none')

        ax.set_title(title)
        ax.set_xlabel('Liczba wierzchołków (n)')
        ax.set_ylabel('Nasycenie (%)')

        # labelpad odsuwa napis od osi Z, zapobiegając nachodzeniu na cyferki
        ax.set_zlabel('Czas [s]', labelpad=12)

        # pad odsuwa pasek skali od całego bloku wykresu
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, pad=0.15)
        fig.savefig(f"Plots/{title}.png")

    plt.show()