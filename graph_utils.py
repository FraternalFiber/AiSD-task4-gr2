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


def edges_to_graph_matrix(n, edges):
    """ Tworzy Macierz Grafu (N x N+4) """
    matrix = [[0] * (n + 4) for _ in range(n)]
    adj = [set() for _ in range(n)]
    predecessors = [0] * n

    for u, v in edges:
        adj[u].add(v)
        predecessors[v] += 1

    for i in range(n):
        # 1. Lista następców (LN i wartości dodatnie)
        succs = sorted(list(adj[i]))
        if succs:
            matrix[i][n] = succs[0] + 1  # LN
            for k in range(len(succs)):
                curr = succs[k]
                next_val = succs[k + 1] + 1 if k + 1 < len(succs) else curr + 1
                matrix[i][curr] = next_val

        # 2. Lista braków (LB i wartości ujemne)
        no_succs = sorted([v for v in range(n) if v not in adj[i]])
        if no_succs:
            matrix[i][n + 2] = no_succs[0] + 1  # LB
            for k in range(len(no_succs)):
                curr = no_succs[k]
                next_val = no_succs[k + 1] + 1 if k + 1 < len(no_succs) else curr + 1
                matrix[i][curr] = -next_val

        matrix[i][n + 1] = predecessors[i]
        if i in adj[i]: matrix[i][n + 3] = i + 1

    return matrix

def generate_random_graph(n, s_pct, is_directed=False):
    if not is_directed:
        max_e = (n * (n - 1)) // 2
        target_e = int(max_e * (s_pct / 100))
        matrix = [[0]*n for _ in range(n)]
        edges_count = 0
        edges_list = []
        while edges_count < target_e:
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            if u != v and matrix[u][v] == 0:
                matrix[u][v] = 1
                matrix[v][u] = 1
                edges_list.append((u, v))
                edges_count += 1
        return matrix, target_e
    else:
        max_e = n * (n - 1)
        target_e = int(max_e * (s_pct / 100))
        edges = []
        while len(edges) < target_e:
            u, v = random.randint(0, n-1), random.randint(0, n-1)
            if u != v and (u, v) not in edges:
                edges.append((u, v))
        return edges_to_graph_matrix(n, edges), target_e