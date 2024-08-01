def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

print(solution("helloWorld"))       # "hello World"
print(solution("camelCase"))        # "camel Case"
print(solution("breakCamelCase"))   # "break Camel Case"