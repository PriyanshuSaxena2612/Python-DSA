# print all factors of a number
# 10 -> [1,2,5,10]
# 15 -> [1,3,5,15]
# 20 -> [1,2,4,5,10,20]

import math
def get_factors(num:int)->list:
    """
    Returns all factors of a positive number
    Args:
        nums(int): Input Number
    Returns:
        list[int]: Sorted list of factors
    """
    factors = []
    if num <= 0:
        raise ValueError("Input must be a positive number")
    for i in range(1, math.isqrt(num)+1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num//i)
    return sorted(factors)
if __name__ == "__main__":
    print(get_factors(8))


def spf(num):
    spf = list(range(num+1))
    for i in range(2, math.isqrt(num)+1):
        if spf[i] == i:
            for j in range(i*i,num+1,i):
                if spf[j] == j:
                    spf[j] = i
    return spf[1:]
print(spf(8))
