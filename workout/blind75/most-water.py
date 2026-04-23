import unittest
from typing import List

# Container with most water
# https://leetcode.com/problems/container-with-most-water/description/
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Area = width * height
# Area = (j - i) * min(height[i], height[j])
def find_max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        # Calculate the area formed by the lines at left and right
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)
        # Move the pointer that points to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


class TestFindMaxArea(unittest.TestCase):

    def test_return_max_area(self):
        # given
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        # when
        result = find_max_area(height)
        # then
        self.assertEqual(result, expected)

    def test_return_max_area_when_n_is_2(self):
        # given
        height = [1, 1]
        expected = 1
        # when
        result = find_max_area(height)
        # then
        self.assertEqual(result, expected)


# python3 -m unittest -v most-water.py
if __name__ == '__main__':
    unittest.main()
