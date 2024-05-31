def solution(string):
# 1st solution
    return string[::-1]
# 2nd solution
    # return ''.join(reversed(string))
# 3rd solution
    # return ''.join([string[i] for i in range(len(string) -1, -1, -1)])
#4th solution
    # reverse_string = ''
    # letter = len(string) - 1
    # for i in string:
    #     reverse_string += string[letter]
    #     letter -= 1
    # return reverse_string


print(solution('hacker')) # rekcah
print(solution('world')) # dlrow
print(solution('hello')) # olleh
print(solution('')) # ''
print(solution('h')) # 'h'