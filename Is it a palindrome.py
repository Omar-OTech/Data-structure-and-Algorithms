def is_palindrome(s):
    # s = s.lower()
    # return s == s[::-1]

# 2nd solution
    s = s.lower()
    for i in range(len(s) // 2):
        print(s[i], s[-i - 1])
        if s[i] != s[-i - 1]:
            return False
    return True


print(is_palindrome('a'))         #   True
print(is_palindrome('aba'))       #   True
print(is_palindrome('Abba'))      #   True
print(is_palindrome('malam'))     #   True
print(is_palindrome('walter'))    #   False
print(is_palindrome('kodok'))     #   True
print(is_palindrome('Kasue'))     #   False