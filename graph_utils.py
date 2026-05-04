import random

def load_graph_from_input():
    print("Podaj V i E (spacja), a następnie kolejne krawędzie/łuki (u v):")
    first_line = input().strip().split()
    n, e = int(first_line[0]), int(first_line[1])
    edges = []
    for _ in range(e):
        u, v = map(int, input().strip().split())
        edges.append((u, v))
    return n, e, edges

def load_graph_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')
    n, e = map(int, lines[0].strip().split())
    edges = []
    for line in lines[1:]:
        if line.strip():
            u, v = map(int, line.strip().split())
            edges.append((u, v))
    return n, e, edges

def edges_to_adj_matrix(n, edges):
    """ Tworzy macierz sąsiedztwa (V x V) dla grafów nieskierowanych """
    matrix = [[0]*n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] += 1
        matrix[v][u] += 1
    return matrix

def edges_to_inc_matrix(n, e_count, edges):
    """ Tworzy Macierz Grafu/Incydencji (V x E) dla multigrafów skierowanych """
    matrix = [[0]*e_count for _ in range(n)]
    for e_idx, (u, v) in enumerate(edges):
        matrix[u][e_idx] = 1   # Wychodzi z u
        matrix[v][e_idx] = -1  # Wchodzi do v
    return matrix

def generate_random_graph(n, s_pct, is_directed=False):
    """ Generuje graf według ustalonego nasycenia i typu struktury """
    if not is_directed:
        # Nieskierowany prosty -> Macierz Sąsiedztwa
        max_e = (n * (n - 1)) // 2
        target_e = int(max_e * (s_pct / 100))
        matrix = [[0]*n for _ in range(n)]
        edges = 0
        while edges < target_e:
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            if u != v and matrix[u][v] == 0:
                matrix[u][v] = 1
                matrix[v][u] = 1
                edges += 1
        return matrix, target_e
    else:
        # Multigraf skierowany -> Macierz Incydencji
        max_e = n * (n - 1)
        target_e = int(max_e * (s_pct / 100))
        matrix = [[0]*target_e for _ in range(n)]
        for e_idx in range(target_e):
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            while u == v: # Unikamy pętli własnych dla spójności
                v = random.randint(0, n-1)
            matrix[u][e_idx] = 1   # Wyjście
            matrix[v][e_idx] = -1  # Wejście
        return matrix, target_e