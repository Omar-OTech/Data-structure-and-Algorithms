def smash(words):
# 1st solution
    return ' '.join(words)

# 2nd solution
    # res = ''
    # for word in words:
    #     if word == words[0]:
    #         res += word + ""
    #     else:
    #         res = res + ' ' + word
    # return res









print(smash(['hello', 'world', 'this', 'is', 'great']))  # Output: 'hello world this is great'
print(smash(['hello', 'world']))              # Output: 'hello world'
print(smash(['single']))                      # Output: 'single'
print(smash([]))                              # Output: ''
print(smash(['Python', 'is', 'fun']))         # Output: 'Python is fun'