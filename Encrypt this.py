def encrypt_this(text):
# 1st solution
    res = ''
    for word in text.split():
# replace the first character with its ASCII value
        if len(word) == 1:
            res += str(ord(word)) + ' '
# replace the first and last character with their ASCII values
        elif len(word) == 2:
            res += str(ord(word[0])) + word[1] + ' '
# replace the first and last character with their ASCII values
        else:
            res += str(ord(word[0])) + word[-1] + word[2:-1] + word[1] + ' '
# return the result
    return res.strip()

print(encrypt_this("Hello"))         # "72olle"
print(encrypt_this("good"))          # "103doo"
print(encrypt_this("hello world"))   # "104olle 119drlo"
print(encrypt_this("A wise old owl lived in an oak"))  # "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
print(encrypt_this("The more he saw the less he spoke"))  # "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
print(encrypt_this("The less he spoke the more he heard"))  # "84eh 108sse 104e 115eokp 116eh 109ero 104e 104uo"
print(encrypt_this("Why can we not all be like that wise old bird"))  # "87yh 99na 119ew 110to 97lla 98e 108eki 116s 104e 119drlo 98ir"
print(encrypt_this("Thank you Piotr for all your help"))  # "84kanh 121uo 80roti 102ro 97lla 108ru 121ru 104ple"
print(encrypt_this("")) # ""