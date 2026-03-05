import math

def rev_num(num):
    rev = 0
    while num >= 1:
        rem = num % 10
        rev = rev*10 + rem
        num //= 10
    return rev

def checkPalindrome(num):
    if num == 0:
        return True
    num_len = int(math.log10(num)) + 1 
    if num_len == 1:
        return True
    half_len = num_len // 2
    first_half = num // (10 ** (num_len - half_len))
    second_half = num % (10 ** half_len)
    second_half = rev_num(second_half)
    return first_half == second_half
print(checkPalindrome(0))
print(checkPalindrome(12321))
print(checkPalindrome(121))
print(checkPalindrome(12344321))





def checkPalindrome02(num):
    if num < 0 or num == 0:
        return True
    rev = 0
    while num > rev:
        rev = rev * 10 + num % 10
        num //= 10
    return (rev == num) or (num == rev // 10)
print(checkPalindrome02(12345))