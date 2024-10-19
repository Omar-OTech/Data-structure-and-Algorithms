def decipher_this(s):
    words = s.split()
    result = []
    for word in words:
        num = ''
        for i in word:
            if i.isdigit():
                num += i
        word = word.replace(num, chr(int(num)))
        if len(word) > 2:
            word = word[0] + word[-1] + word[2:-1] + word[1]
        result.append(word)
    return ' '.join(result)





print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))                    # "A wise old owl lived in an oak"
print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"))                # "The more he saw the less he spoke"
print(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"))              # "The less he spoke the more he heard"
print(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"))  # "Why can we not all be like that wise old bird"
print(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"))                    # "Thank you Piotr for all your help"