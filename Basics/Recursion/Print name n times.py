# # Print name n times

def print_names01(n):
    if n == 0:
        return
    print("Priyanshu")
    print_names01(n-1)

print_names01(4)


count = 0
def print_names02():
    global count
    if count == 4:
        return
    print("Priyanshu")
    count += 1
    print_names02()

print_names02()