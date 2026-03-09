# Reverse an array using recusion

def rev_arr(arr: list, start: int = 0, end: int = 0) -> None:
    if start > end //2:
        print(arr)
        return
    arr[start], arr[end - 1] = arr[end - 1], arr[start]
    rev_arr(arr, start+1, end-1)

rev_arr([1,2,3,4,5],0,3)
rev_arr([1,2,3,4],0,4)