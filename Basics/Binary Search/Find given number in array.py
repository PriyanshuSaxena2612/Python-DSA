# Find given number in array

def find_number(arr:list, target:int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high-low)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(find_number([2,4,6,7,9,11,18,19],6))