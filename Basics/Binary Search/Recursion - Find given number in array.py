# Recursion - Find given number in array
def find_num(arr:list,target:int,low:int,high:int):
    if low > high:
        return -1
    mid = low + (high - low)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        return find_num(arr,target,low,mid-1)
    else:
        return find_num(arr,target,mid+1,high)

print(find_num([1,2,3,4,5],2,0,4))