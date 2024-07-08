def capitals(word):
# 1st solution
    return [i for i in range(len(word)) if word[i].isupper()] 

# # 2nd solution
    # upper = []
    # for i in range(len(word)):
    #     if word[i].isupper():
    #         upper.append(i)
    # return upper
    
print(capitals('CodEWaRs'))  # [0,3,4,6]