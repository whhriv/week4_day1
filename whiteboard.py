
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

def solution(nums):
    max_cons = 0
    cons_ = []
    for num in nums:
        if num == 1:
            max_cons += 1
        else:
            cons_.append(max_cons)
            max_cons = 0
    cons_.append(max_cons)
    return max(cons_)


def solution(nums):
    str_nums = ''.join([str(num) for num in nums])
    print(str_nums)

    ones = str_nums.split('0')
    print(ones)
    consec_count = [len(one) for one in ones]
    print(consec_count)
    return max(consec_count)

def solution(nums):
    return max(len(consec) for consec in ''.join([str(num) for num in nums]).split('0'))


          
    





























# def solution(nums):
#     consecutive_nums = 0
#     max_consecutive = 0
#     for num in nums:
#         if num:
#             consecutive_nums += 1
#         else:
#             if consecutive_nums > max_consecutive:
#                 max_consecutive = consecutive_nums
#             consecutive_nums = 0
#     if consecutive_nums > max_consecutive:
#         max_consecutive = consecutive_nums
#     return max_consecutive