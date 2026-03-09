# Print 1 to N using recursion

def print_n_backtrack(n):
    if n == 0:
        return
    print_n_backtrack(n-1)
    print(n)

print_n_backtrack(3)


def print_n_forward(n,k):
    if k == n+1:
        return
    print(k)
    print_n_forward(n,k+1)
print_n_forward(3,1)
