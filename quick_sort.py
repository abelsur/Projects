import sys
import time
# abel surafel quick sort
def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        p, r = stack.pop()
        if p < r:
            q = partition(arr, p, r)
            stack.append((p, q - 1))
            stack.append((q + 1, r))
    return arr

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def read_dataset(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    try:
        count = int(lines[0])
        if count == len(lines) - 1:
            data = [float(x) for x in lines[1:]]
        else:
            data = [float(x) for x in lines]
    except ValueError:
        data = [float(x) for x in lines]
    return data

def write_output(path, numbers):
    with open(path, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python quick_sort.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_dataset(input_file)
    print(f"Sorting {len(data)} numbers from {input_file} ...")

    start_time = time.time()
    sorted_data = quick_sort(data)
    end_time = time.time()

    runtime_ms = (end_time - start_time) * 1000
    print(f"Sorting completed in {runtime_ms:.3f} milliseconds.")

    write_output(output_file, sorted_data)
    print(f"Sorted output written to {output_file}")

if __name__ == "__main__":
    main()
