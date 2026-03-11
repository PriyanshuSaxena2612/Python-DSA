# Generate Subsequence with sum K

def generate_subsequence(arr: list, k: int, index, subset, result, sum = 0):
    if index >= len(arr):
        if sum == k:
            result.append(subset.copy())
            print(result)
        return
    subset.append(arr[index])
    generate_subsequence(arr, k, index+1, subset, result, sum + arr[index])
    subset.pop()
    generate_subsequence(arr, k, index+1, subset, result, sum)

generate_subsequence([3,3,-3],3,0,[],[],0)
