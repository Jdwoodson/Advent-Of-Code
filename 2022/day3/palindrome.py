def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
    
    
print(isPalindrome(101))
# True

print(isPalindrome(1210))
# False