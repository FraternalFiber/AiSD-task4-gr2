import sys
from algorithms import ahs, ahg, aes, aeg
from graph_utils import load_graph_from_input, load_graph_from_file, edges_to_adj_matrix, edges_to_inc_matrix
from benchmarks import run_tests
from report import print_markdown_report, plot_3d_surfaces


def manual_test():
    print("\n--- Tryb Manualny ---")
    print("1. Wczytaj graf z klawiatury")
    print("2. Wczytaj graf z pliku")
    choice = input("Wybór: ")

    if choice == '1':
        n, e, edges = load_graph_from_input()
    elif choice == '2':
        filepath = input("Podaj ścieżkę do pliku (np. graf1.txt): ")
        n, e, edges = load_graph_from_file(filepath)
    else:
        print("Błędny wybór.")
        return

    is_dir_input = input("Czy graf jest skierowany? (T/N): ").strip().upper()
    is_directed = True if is_dir_input == 'T' else False

    if not is_directed:
        matrix = edges_to_adj_matrix(n, edges)
        print("\nSzukanie cyklu Hamiltona (AHS - Macierz Sąsiedztwa)...")
        h_cycle = ahs(matrix, n)

        print("Szukanie cyklu Eulera (AES - Macierz Sąsiedztwa)...")
        e_cycle = aes(matrix, n, e)
    else:
        matrix = edges_to_inc_matrix(n, e, edges)
        print("\nSzukanie cyklu Hamiltona (AHG - Macierz Grafu/Incydencji)...")
        h_cycle = ahg(matrix, n, e)

        print("Szukanie cyklu Eulera (AEG - Macierz Grafu/Incydencji)...")
        e_cycle = aeg(matrix, n, e)

    if h_cycle:
        print("Znaleziono cykl Hamiltona:", h_cycle)
    else:
        print("Graf jest acykliczny pod kątem cyklu Hamiltona / brak cyklu.")

    if e_cycle:
        print("Znaleziono cykl Eulera:", e_cycle)
    else:
        print("Graf jest acykliczny pod kątem cyklu Eulera / brak cyklu.")


def main():
    while True:
        print("\n" + "=" * 30)
        print("--- PROJEKT: ALGORYTMY Z POWRACANIEM ---")
        print("1. Uruchom pojedynczy test (klawiatura/plik)")
        print("2. Uruchom testy wydajnościowe")
        print("3. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            manual_test()
        elif choice == '2':
            results, raw_report = run_tests()
            print_markdown_report(raw_report)
            print("\nWyświetlanie wykresów w nowym oknie (zamknij okno, aby kontynuować)...")
            plot_3d_surfaces(results)
        elif choice == '3':
            sys.exit(0)
        else:
            print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    main()