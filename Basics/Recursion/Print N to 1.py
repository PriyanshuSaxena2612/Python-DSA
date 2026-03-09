# Print N to 1 using recusion

def print_n_forward(n):
    if n == 0:
        return
    print(n)
    print_n_forward(n-1)
print_n_forward(3)

def print_n_backtracking(n,k):
    if k == n+1:
        return
    print_n_backtracking(n,k+1)
    print(k)

print_n_backtracking(3,1)