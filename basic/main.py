# one line comment
""" Multi line
    comment
"""
import sys

words = ['one', 'two']
a = True
if a:
    words.append('tree')
    print('true')
else:
    words.append('four')
    print('false')

print(words)

numbers = [7, 2, -5, 1, 1, -1, 5, -5]


def subarray_sum_on3(nums, k):
    answer = 0
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            subarray_sum = 0
            for i in range(start, end + 1):
                subarray_sum += nums[i]
            if subarray_sum == k:
                answer += 1
    return answer


print(subarray_sum_on3(numbers, 5))


def subarray_sum_on2(nums, k):
    answer = 0
    for start in range(len(nums)):
        subarray_sum = 0
        for i in range(start, len(nums)):
            subarray_sum += nums[i]
            if subarray_sum == k:
                answer += 1
    return answer


print(subarray_sum_on2(numbers, 5))

numbers = [4, 2, 2, 1, 2, -3, 5, -8]


def subarray_sum_on(nums, k):
    answer = 0
    subarray_sum = 0
    prefix_sum_count = {0: 1}
    for i in range(len(nums)):
        subarray_sum += nums[i]
        to_remove = subarray_sum - k
        answer += prefix_sum_count.get(to_remove, 0)
        prev_count = prefix_sum_count.get(subarray_sum, 0)
        prefix_sum_count[subarray_sum] = prev_count + 1
    return answer


print(subarray_sum_on(numbers, 5))

print(sys.builtin_module_names)
print(sys.path)
print(dir())


