def solution(nums):
    answer = 0
    arr = set()
    for x in nums:
        arr.add(x)
    
    max_num = len(nums) // 2
    return min(max_num, len(arr))
    
