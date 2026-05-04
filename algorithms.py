import copy


# ==========================================
# CYKL HAMILTONA
# ==========================================

def ahs(adj_matrix, n):
    """ Algorytm Robertsa-Floresa, macierz sąsiedztwa (graf prosty nieskierowany) """
    path = [0]
    visited = [False] * n
    visited[0] = True

    def backtrack(u):
        if len(path) == n:
            if adj_matrix[u][path[0]] > 0:
                return path + [path[0]]
            return None

        for v in range(n):
            if adj_matrix[u][v] > 0 and not visited[v]:
                visited[v] = True
                path.append(v)
                res = backtrack(v)
                if res: return res
                path.pop()
                visited[v] = False
        return None

    return backtrack(0)


def ahg(inc_matrix, n, e_count):
    """ Algorytm Robertsa-Floresa, macierz grafu (multigraf skierowany) """
    path = [0]
    visited = [False] * n
    visited[0] = True

    def backtrack(u):
        if len(path) == n:
            # Szukamy łuku powrotnego z u do startu (path[0])
            for edge_idx in range(e_count):
                if inc_matrix[u][edge_idx] == 1 and inc_matrix[path[0]][edge_idx] == -1:
                    return path + [path[0]]
            return None

        for edge_idx in range(e_count):
            if inc_matrix[u][edge_idx] == 1:  # Łuk wychodzi z u
                # Znajdź wierzchołek docelowy (gdzie łuk wchodzi)
                dest = -1
                for v in range(n):
                    if inc_matrix[v][edge_idx] == -1:
                        dest = v
                        break

                if dest != -1 and not visited[dest]:
                    visited[dest] = True
                    path.append(dest)
                    res = backtrack(dest)
                    if res: return res
                    path.pop()
                    visited[dest] = False
        return None

    return backtrack(0)


# ==========================================
# CYKL EULERA
# ==========================================

def _count_reachable_adj(matrix, u, n):
    visited = [False] * n
    q = [u]
    visited[u] = True
    count = 1
    while q:
        curr = q.pop(0)
        for v in range(n):
            if matrix[curr][v] > 0 and not visited[v]:
                visited[v] = True
                count += 1
                q.append(v)
    return count


def aes(adj_matrix, n, total_edges):
    """ Algorytm Fleury'ego, macierz sąsiedztwa (graf prosty nieskierowany) """
    if n == 0 or total_edges == 0: return None
    M = copy.deepcopy(adj_matrix)
    path = [0]
    u = 0

    for _ in range(total_edges):
        valid_edges = []
        for v in range(n):
            if M[u][v] > 0:
                valid_edges.append(v)

        if not valid_edges: return None  # Acykliczny

        next_v = valid_edges[0]
        if len(valid_edges) > 1:
            for v in valid_edges:
                reach_before = _count_reachable_adj(M, u, n)
                M[u][v] -= 1;
                M[v][u] -= 1
                reach_after = _count_reachable_adj(M, u, n)
                M[u][v] += 1;
                M[v][u] += 1

                if reach_after == reach_before:
                    next_v = v
                    break

        M[u][next_v] -= 1
        M[next_v][u] -= 1
        path.append(next_v)
        u = next_v

    if len(path) == total_edges + 1 and path[0] == path[-1]:
        return path
    return None


def _count_reachable_inc(matrix, u, n, e_count, used_edges):
    visited = [False] * n
    q = [u]
    visited[u] = True
    count = 1
    while q:
        curr = q.pop(0)
        for edge_idx in range(e_count):
            if not used_edges[edge_idx] and matrix[curr][edge_idx] == 1:
                # Znajdź destynację dla tego łuku
                for v in range(n):
                    if matrix[v][edge_idx] == -1 and not visited[v]:
                        visited[v] = True
                        count += 1
                        q.append(v)
                        break
    return count


def aeg(inc_matrix, n, e_count):
    """ Algorytm Fleury'ego, macierz grafu (multigraf skierowany) """
    if n == 0 or e_count == 0: return None
    used_edges = [False] * e_count
    path = [0]
    u = 0

    for _ in range(e_count):
        valid_edges = []  # Lista par (indeks_luku, wierzcholek_docelowy)
        for edge_idx in range(e_count):
            if not used_edges[edge_idx] and inc_matrix[u][edge_idx] == 1:
                dest = -1
                for v in range(n):
                    if inc_matrix[v][edge_idx] == -1:
                        dest = v
                        break
                valid_edges.append((edge_idx, dest))

        if not valid_edges: return None  # Utknęliśmy

        chosen_edge, next_v = valid_edges[0]

        if len(valid_edges) > 1:
            for edge_idx, dest in valid_edges:
                reach_before = _count_reachable_inc(inc_matrix, u, n, e_count, used_edges)
                used_edges[edge_idx] = True  # Symulacja usunięcia
                reach_after = _count_reachable_inc(inc_matrix, u, n, e_count, used_edges)
                used_edges[edge_idx] = False  # Przywrócenie

                # Jeśli to nie jest most, bierzemy to
                if reach_after == reach_before:
                    chosen_edge, next_v = edge_idx, dest
                    break

        used_edges[chosen_edge] = True
        path.append(next_v)
        u = next_v

    if len(path) == e_count + 1 and path[0] == path[-1]:
        return path
    return None