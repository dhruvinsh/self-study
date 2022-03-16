"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Leetcode#11
Task: You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
"""

from utils import time_it


@time_it
def max_area(height: list[int]) -> int:
    """find max available water area covered by the vertical line.

    Steps:
    - assign two pointer `left` and `right` and assume area is -1
    - start calculating current area by finding minmum of left and right
    height and multiply with distance between two pointer.
    - move the pointer which has small height and continue calculating area
    till left pointer is lower then right pointer

    Complexity:
    Time: O(N)
    Space: O(1)

    Args:
        height (list[int]): array of height

    Returns:
        max available are for water
    """
    area = -1
    left = 0
    right = len(height) - 1

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        area = max(area, current_area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return area


if __name__ == "__main__":
    HEIGHTS = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],  # 46
        [1, 1],  # 1
        [4, 3, 2, 1, 4],  # 16
        [1, 2, 1],  # 2
    ]

    for h in HEIGHTS:
        MAX_AREA = max_area(h)
        print(f"Max water area is: {MAX_AREA}")
