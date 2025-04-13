# Sliding Window Algorithm
def find_max_consecutive_ones(nums):
    count = 0
    m = 0
    for num in nums:
        if num == 1:
            count = count + 1
        else:
            count = 0
        m = max(count, m)
    return m


n = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
print(find_max_consecutive_ones(n))