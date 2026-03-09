# Sum of 1 to N using Recursion

def print_sum01(n,sum_ = 0):
    if n == 0:
        print(sum_)
        return
    sum_ += n
    print_sum01(n-1,sum_)

print_sum01(5)

def print_sum02(n):
    if n == 0:
        return 0
    return n + print_sum02(n - 1)

print(print_sum02(5))