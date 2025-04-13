from collections import Counter

# The Boyer-Moore voting algorithm is one of the popular optimal algorithms
# which is used to find the majority element among the given elements that have more than N/ 2 occurrences.
# This works perfectly fine for finding the majority element which takes 2 traversals over the given elements,
# which works in O(N) time complexity and O(1) space complexity.
#
# Let us see the algorithm and intuition behind its working, by taking an example
# Input :{1,1,1,1,2,3,5}
# Output : 1
# Explanation : 1 occurs more than 3 times.
# Input : {1,2,3}
# Output : -1
# This algorithm works on the fact that if an element occurs more than N/2 times,
# it means that the remaining elements other than this would definitely be less than N/2
# Intuition Behind Working :
# When the elements are the same as the candidate element,
# votes are incremented whereas when some other element is found (not equal to the candidate element),
# we decreased the count.


def find_majority_elements_bf(nums):
    counter = Counter(nums)
    max_cnt = -1
    ans = nums[0]
    for key, val in counter.items():
        if val > max_cnt:
            max_cnt = val
            ans = key
    return ans


def find_majority_elements(nums):
    # Boyer-Moore voting algorithm
    candidate = None
    cnt = 0
    for num in nums:
        if cnt == 0:
            candidate = num
        cnt += 1 if candidate == num else -1
    return candidate


print(find_majority_elements([2, 2, 1, 1, 1, 2, 2]))

print(find_majority_elements([1, 1, 1, 1, 2, 3, 5]))
