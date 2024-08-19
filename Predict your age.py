def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    arr = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    multipling = []
    for i in arr:
        multipling.append(i*i)
    return sum(multipling) ** 0.5 // 2

# 2nd solution
    # def predict_age(*ages):
    #     return sum(a*a for a in ages)**.5//2

print(predict_age(65,60,75,55,60,63,64,45))   # 86