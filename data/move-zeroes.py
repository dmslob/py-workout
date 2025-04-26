def move_zeroes(nums: list[int]):
    insert_pos = 0
    # First pass: move non-zero elements forward
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    # Second pass: fill the rest with zeros
    for i in range(insert_pos, len(nums)):
        nums[i] = 0


n = [0, 1, 0, 3, 12]
move_zeroes(n)
print(n)  # Output: [1, 3, 12, 0, 0]
