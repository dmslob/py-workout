from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n
    for i in range(n):
        j = -i - 1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]
    return [l * r for l, r in zip(l_arr, r_arr)]


arr = [1, 2, 3, 4]
print(product_except_self(arr))
