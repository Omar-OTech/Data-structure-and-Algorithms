def count_positives_sum_negatives(arr):
# 1st solution
    if arr == []:
        return []
    else:
        count = 0
        sum = 0
        for i in arr:
            if i > 0:
                count += 1
            else:
                sum += i
        return [count, sum]

# 2nd solution
    # pos = sum(1 for i in arr if i > 0)
    # neg = sum(i for i in arr if i < 0)
    # return [pos, neg] if len(arr) > 0 else []





print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) #[10,-65]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])) #[8,-50]
print(count_positives_sum_negatives([1])) #[1,0]
print(count_positives_sum_negatives([-1])) #[0,-1]
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0])) #[0,0]
print(count_positives_sum_negatives([])) #[]