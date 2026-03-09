# Find factorial of a number using recusion

# Functional Recusion Call
def find_factorial(n):
    if n == 1:
        return 1
    return n * find_factorial(n - 1)

print(find_factorial(5))


# Parameterized Recusion Call
def find_factorial_param(n,fact):
    if n == 1:
        print(fact)
        return
    fact *= n
    find_factorial_param(n-1,fact)

find_factorial_param(4,1)