# Generate All Subseqences

def generate_subseqences(arr, subset: list = [], result: list = [], index: int = 0):
    if index >= len(arr):
        print(result)
        result.append(subset.copy())
        return
    subset.append(arr[index])
    generate_subseqences(arr, subset, result, index+1)
    subset.pop()
    generate_subseqences(arr, subset, result, index+1)

generate_subseqences([5,6,7])