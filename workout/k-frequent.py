from typing import List
import heapq
from collections import Counter

# Given an integer array nums and an integer k,
# return the k most frequent elements.
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 4
# Output: [1, 2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


# Time: O(n * log(k)), Space: O(n)
def top_k_frequent_by_heap(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    heap = []
    for key, val in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            heapq.heappushpop(heap, (val, key))
    return [h[1] for h in heap]


# Time: O(n), Space: O(n)
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n + 1)
    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
    return ret


nmbs = [1, 1, 1, 2, 2, 3]
print(top_k_frequent(nmbs, 2))
print(top_k_frequent_by_heap(nmbs, 2))
