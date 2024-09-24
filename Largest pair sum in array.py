def largest_pair_sum(numbers):
    sorted_arr = sorted(numbers)
    return sum(sorted_arr[-2:])



print(largest_pair_sum([10,14,2,23,19]))              # 42
print(largest_pair_sum([-100,-29,-24,-19,19]))        # 0
print(largest_pair_sum([1,2,3,4,6,-1,2]))             # 10
print(largest_pair_sum([-10, -8, -16, -18, -19]))     # -18
