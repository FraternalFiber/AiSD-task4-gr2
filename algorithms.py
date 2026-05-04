import copy


# --- POMOCNICZE DLA MACIERZY GRAFU ---
def get_successors(matrix, u, n):
    succs = []
    curr_ptr = matrix[u][n]  # Kolumna LN
    while curr_ptr > 0:
        v = curr_ptr - 1
        succs.append(v)
        next_ptr = matrix[u][v]
        if next_ptr > 0 and next_ptr != curr_ptr:
            curr_ptr = next_ptr
        else:
            break
    return succs


# --- HAMILTON ---
def ahs(adj_matrix, n):
    path = [0] 
    visited = [False] * n
    visited[0] = True

    def backtrack(u):
        if len(path) == n:
            return path + [path[0]] if adj_matrix[u][path[0]] > 0 else None
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


def ahg(mg_matrix, n):
    path = [0]
    visited = [False] * n
    visited[0] = True

    def backtrack(u):
        if len(path) == n:
            return path + [path[0]] if path[0] in get_successors(mg_matrix, u, n) else None
        for v in get_successors(mg_matrix, u, n):
            if not visited[v]:
                visited[v] = True
                path.append(v)
                res = backtrack(v)
                if res: return res
                path.pop()
                visited[v] = False
        return None

    return backtrack(0)


# --- EULER ---
def _count_reachable_mg(temp_adj, u, n):
    visited = [False] * n
    q = [u]
    visited[u] = True
    count = 1
    while q:
        curr = q.pop(0)
        for v in temp_adj[curr]:
            if not visited[v]:
                visited[v] = True
                count += 1
                q.append(v)
    return count


def aeg(mg_matrix, n, e_count):
    # Fleury wymaga usuwania krawędzi, więc budujemy roboczą listę sąsiedztwa (multigraf)
    temp_adj = [[] for _ in range(n)]
    for u in range(n):
        temp_adj[u] = get_successors(mg_matrix, u, n)

    path = [0]
    u = 0
    # W multigrafie skierowanym musimy przejść dokładnie e_count łuków
    for _ in range(e_count):
        options = temp_adj[u]
        if not options: break

        chosen_v = options[0]
        if len(options) > 1:
            for v in options:
                r_before = _count_reachable_mg(temp_adj, u, n)
                temp_adj[u].remove(v)
                r_after = _count_reachable_mg(temp_adj, u, n)
                temp_adj[u].append(v)
                if r_after == r_before:
                    chosen_v = v
                    break

        temp_adj[u].remove(chosen_v)
        path.append(chosen_v)
        u = chosen_v

    return path if len(path) == e_count + 1 else None


# AES pozostaje bez zmian (używa adj_matrix)
def aes(adj_matrix, n, e_count):
    M = copy.deepcopy(adj_matrix)
    path = [0]
    u = 0

    def count_r(mat, start, size):
        vis = [False] * size
        q = [start]
        vis[start] = True
        c = 1
        while q:
            curr = q.pop(0)
            for v in range(size):
                if mat[curr][v] > 0 and not vis[v]:
                    vis[v] = True
                    c += 1
                    q.append(v)
        return c

    for _ in range(e_count):
        valid = [v for v in range(n) if M[u][v] > 0]
        if not valid: break
        next_v = valid[0]
        if len(valid) > 1:
            for v in valid:
                b = count_r(M, u, n)
                M[u][v] -= 1
                M[v][u] -= 1
                a = count_r(M, u, n)
                M[u][v] += 1
                M[v][u] += 1
                if a == b: next_v = v; break
        M[u][next_v] -= 1
        M[next_v][u] -= 1
        path.append(next_v)
        u = next_v
    return path if len(path) == e_count + 1 else None