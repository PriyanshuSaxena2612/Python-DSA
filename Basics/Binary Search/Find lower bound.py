# Find lower bound

def find_lower_bound(arr:list,target:int,low:int,high:int):
    low,high=0,len(arr)
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid] >= target:
            low = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid+1
    return low

arr = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
print(find_lower_bound(arr,12,0,len(arr)))