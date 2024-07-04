def solution(nums):
    return [] if nums is None else sorted(nums)


# 2nd solution
def solution(nums):
    if nums == []:
        return []
    if nums is None:
        return []
    else:
        return sorted(nums)

print(solution([1,2,3,10,5]))    #   [1,2,3,5,10]
print(solution(None))            #   []
print(solution([]))              #   []
print(solution([20,2,10]))       #   [2,10,20]
print(solution([2,20,10]))       #   [2,10,20]