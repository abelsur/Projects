import sys
import time

#abel surafel insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# read all numbers
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

# writing sorted #'s to an output file 
def write_output(path, numbers):   
    with open(path, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python insertion_sort.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_dataset(input_file)
    print(f"Sorting {len(data)} numbers from {input_file} ...")

    start_time = time.time()
    sorted_data = insertion_sort(data)
    end_time = time.time()

    runtime_ms = (end_time - start_time) * 1000
    print(f"Sorting completed in {runtime_ms:.3f} milliseconds.")

    write_output(output_file, sorted_data)
    print(f"Sorted output written to {output_file}")


if __name__ == "__main__":
    main()
