# abel surafel assignment 2

import math
import glob
import os

def euclidean_distance(a, b):
    
    return math.sqrt((a - b) ** 2)   # euclidean form


def dtw(x, y):
    N = len(x)
    M = len(y)

    D = [[float('inf')] * M for _ in range(N)]

    # Initialization
    D[0][0] = euclidean_distance(x[0], y[0])

    # First column
    for i in range(1, N):
        D[i][0] = euclidean_distance(x[i], y[0]) + D[i - 1][0]

    # First row
    for j in range(1, M):
        D[0][j] = euclidean_distance(x[0], y[j]) + D[0][j - 1]

    # Recurrence
    for i in range(1, N):
        for j in range(1, M):
            cost = euclidean_distance(x[i], y[j])
            D[i][j] = cost + min(
                D[i - 1][j],     # (insertion in Y)
                D[i][j - 1],     # (insertion in X)
                D[i - 1][j - 1]  # (match)
            )

    total_cost = D[N - 1][M - 1]

    # backtracking
    path = []
    i, j = N - 1, M - 1
    path.append((i, j))

    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            # choose predecessor that gave the min
            prev_costs = [
                D[i - 1][j],     # up
                D[i][j - 1],     # left
                D[i - 1][j - 1]  # diag
            ]
            arg_min = prev_costs.index(min(prev_costs))
            if arg_min == 0:
                i -= 1
            elif arg_min == 1:
                j -= 1
            else:
                i -= 1
                j -= 1
        path.append((i, j))

    path.reverse()  # from start to end
    return total_cost, path

def read_dtw_input(path):

    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # First line has the lengths (we don't really need them, but we can check)
    n, m = map(int, lines[0].split())

    x = list(map(float, lines[1].split()))
    y = list(map(float, lines[2].split()))

    return x, y

def print_dtw_alignment(x, y, cost, path):
   
    print("Input 1:", x)
    print("Input 2:", y)
    print("Warping Path:", path)
    print("Total DTW Cost:", cost)
    print()  # blank line between tests

def run_single_file(path):
    x, y = read_dtw_input(path)
    cost, wpath = dtw(x, y)
    print("=" * 60)
    print(f"Results for {os.path.basename(path)}")
    print("=" * 60)
    print_dtw_alignment(x, y, cost, wpath)

if __name__ == "__main__":
    # Automatically find all data/input*.txt files
    input_files = sorted(glob.glob("data/input*.txt"))

    if not input_files:
        print("No input files found in ./data (expected data/input*.txt).")
    else:
        for fname in input_files:
            run_single_file(fname)