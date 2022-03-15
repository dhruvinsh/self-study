"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Leetcode#941
Task: Given an array of integers `arr`, return true if and only if it is a
valiid mountain array.
`arr` is a mountain array if and only if:
- arr.length >= 3
- there exists some i with 0 < i < arr.length -1 such that:
    arr[0] < arr[1] < .. < arr[i]
    arr[i] > arr[i+1] > .. arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""

from utils import time_it


@time_it
def valid_mountain(array: list[int]) -> bool:
    """this method validates if array is valid mountain.

    Steps:
    - intialize pointer at index 1.
    - while loop to check increment `while(i<len(array) and array[i] > array[i-1])`
    - if pointer moved, then i should not be equal to 1. but should not
      be len(array) either else it suggests that array just keep
      increasing.
    - run another while loop to check decrement. (think how?)
    - if all correct then i should be equal to len(array).

    Complexity:
    Time: O(2N) -> O(N)
    Space: O(1)

    Args:
        array (list[int]): list of integers.

    Returns:
        boolean, True if valid mountain array else False
    """
    n = len(array)
    # not a valid array size
    if n < 3:
        return False

    # starting index set to 1
    i = 1
    while i < n and array[i] > array[i - 1]:
        i += 1

    # if i still 1 then pointer did not move at all, thats bad
    # or if i is equal to length of array then its increasing array
    if i in (1, n - 1):
        return False

    while i < n and array[i] < array[i - 1]:
        i += 1

    return i == n


if __name__ == "__main__":
    TEST_ARRAYS = [
        [3, 5],  # invalid
        [3, 5, 5],  # invalid
        [3, 5, 6],  # valid
        [1, 4, 6, 8, 8, 3, 2, 0],  # invalid
        [1, 4, 6, 8, 6, 3, 2, 10],  # invalid
        [1, 4, 6, 8, 6, 3, 2, 0],  # valid
    ]

    for arr in TEST_ARRAYS:
        RESULT = valid_mountain(arr)
        print(f"Mountain array validation: {RESULT}\n")
