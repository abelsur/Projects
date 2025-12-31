import sys
import time
# abel surafel heap sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# sort in ascending order
def heap_sort(arr):
    n = len(arr)

    # max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr

# read all #'s in file
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
        print("Usage: python heap_sort.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_dataset(input_file)
    print(f"Sorting {len(data)} numbers from {input_file} ...")

    start_time = time.time()
    sorted_data = heap_sort(data)
    end_time = time.time()

    runtime_ms = (end_time - start_time) * 1000
    print(f"Sorting completed in {runtime_ms:.3f} milliseconds.")

    write_output(output_file, sorted_data)
    print(f"Sorted output written to {output_file}")


if __name__ == "__main__":
    main()
