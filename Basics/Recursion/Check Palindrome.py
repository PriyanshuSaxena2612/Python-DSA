# Check Palindrome using recursion

def check_palindrome(s: str, start: int, end: int) -> None:
    if start >= end:
        return True
    return (s[start] == s[end-1]) and check_palindrome(s, start+1, end-1)
    

print(check_palindrome('abc',0,3))
print(check_palindrome('acca',0,4))