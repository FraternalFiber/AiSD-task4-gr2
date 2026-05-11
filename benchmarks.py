import time
from algorithms import ahs, ahg, aes, aeg
from graph_utils import generate_random_graph
from report import print_live_markdown_block


def _get_sample_edges(matrix, limit=5, is_directed=False):
    """ Wyciąga do 5 krawędzi (dokładnie takich, jakie znalazłyby się w pliku TXT) """
    edges = []
    n = len(matrix)
    for u in range(n):
        for v in range(n):
            if not is_directed and v < u:
                continue  # Nieskierowany: pomijamy duplikaty z dolnego trójkąta
            weight = matrix[u][v]
            for _ in range(weight):
                edges.append(f"{u} {v}")
                if len(edges) >= limit:
                    return edges
    return edges


def run_tests():
    n_values = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    s_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    results = {
        'AHS': {'n': [], 's': [], 'time': []},
        'AES': {'n': [], 's': [], 'time': []},
        'AHG': {'n': [], 's': [], 'time': []},
        'AEG': {'n': [], 's': [], 'time': []}
    }

    print("# Raport z wykonania algorytmów z powracaniem\n")

    for n in n_values:
        for s in s_values:
            # === 1. Graf Nieskierowany ===
            mat_undir, e_undir = generate_random_graph(n, s, is_directed=False)

            start = time.perf_counter()
            res_ahs = ahs(mat_undir, n)
            t_ahs = time.perf_counter() - start

            start = time.perf_counter()
            res_aes = aes(mat_undir, n, e_undir)
            t_aes = time.perf_counter() - start

            # === 2. Multigraf Skierowany ===
            mat_dir, e_dir = generate_random_graph(n, s, is_directed=True)

            start = time.perf_counter()
            res_ahg = ahg(mat_dir, n)
            t_ahg = time.perf_counter() - start

            start = time.perf_counter()
            res_aeg = aeg(mat_dir, n, e_dir)
            t_aeg = time.perf_counter() - start

            # Zapis danych do słownika (dla wykresów)
            results['AHS']['n'].append(n);
            results['AHS']['s'].append(s);
            results['AHS']['time'].append(t_ahs)
            results['AES']['n'].append(n);
            results['AES']['s'].append(s);
            results['AES']['time'].append(t_aes)
            results['AHG']['n'].append(n);
            results['AHG']['s'].append(s);
            results['AHG']['time'].append(t_ahg)
            results['AEG']['n'].append(n);
            results['AEG']['s'].append(s);
            results['AEG']['time'].append(t_aeg)

            # Pobranie max. 5 pierwszych krawędzi (jak z pliku wejściowego)
            edges_sample_undir = _get_sample_edges(mat_undir, limit=5, is_directed=False)
            edges_sample_dir = _get_sample_edges(mat_dir, limit=5, is_directed=True)

            # === Drukuj na bieżąco raport w formacie Markdown ===
            print_live_markdown_block(
                n, s,
                e_undir, edges_sample_undir,
                e_dir, edges_sample_dir,
                res_ahs, t_ahs, res_aes, t_aes,
                res_ahg, t_ahg, res_aeg, t_aeg
            )

    return results