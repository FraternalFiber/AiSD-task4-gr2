import time
from algorithms import ahs, ahg, aes, aeg
from graph_utils import generate_random_graph


def run_tests():
    n_values = list(range(6, 16))
    s_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    results = {
        'AHS': {'n': [], 's': [], 'time': []},
        'AES': {'n': [], 's': [], 'time': []},
        'AHG': {'n': [], 's': [], 'time': []},
        'AEG': {'n': [], 's': [], 'time': []}
    }
    raw_data_report = []

    print("Rozpoczynam testy eksperymentalne...")

    for n in n_values:
        for s in s_values:
            # 1. Graf Nieskierowany - Macierz Sąsiedztwa
            mat_undir, e_undir = generate_random_graph(n, s, is_directed=False)

            # AHS (Hamilton)
            start = time.perf_counter()
            res_ahs = ahs(mat_undir, n)
            results['AHS']['n'].append(n);
            results['AHS']['s'].append(s);
            results['AHS']['time'].append(time.perf_counter() - start)

            # AES (Euler)
            start = time.perf_counter()
            res_aes = aes(mat_undir, n, e_undir)
            results['AES']['n'].append(n);
            results['AES']['s'].append(s);
            results['AES']['time'].append(time.perf_counter() - start)

            raw_data_report.append(
                ("Nieskierowany (Sąsiedztwa)", n, s, results['AHS']['time'][-1], "TAK" if res_ahs else "NIE",
                 results['AES']['time'][-1], "TAK" if res_aes else "NIE"))

            # 2. Multigraf Skierowany - Macierz Incydencji
            mat_dir, e_dir = generate_random_graph(n, s, is_directed=True)

            # AHG (Hamilton)
            start = time.perf_counter()
            res_ahg = ahg(mat_dir, n, e_dir)
            results['AHG']['n'].append(n);
            results['AHG']['s'].append(s);
            results['AHG']['time'].append(time.perf_counter() - start)

            # AEG (Euler)
            start = time.perf_counter()
            res_aeg = aeg(mat_dir, n, e_dir)
            results['AEG']['n'].append(n);
            results['AEG']['s'].append(s);
            results['AEG']['time'].append(time.perf_counter() - start)

            raw_data_report.append(
                ("Skierowany (Incydencji)", n, s, results['AHG']['time'][-1], "TAK" if res_ahg else "NIE",
                 results['AEG']['time'][-1], "TAK" if res_aeg else "NIE"))

    return results, raw_data_report