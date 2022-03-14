"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Algorithm: Binary Search

Most popular search algorithm to find element in a collection eg array
But collections need to be sorted first. Then and then Binary search
is applicable

Task: from a given long array, find the index of given element, if given
element is not present then as a result return -1. Do not use list membership
operator here
"""


def binary_search(array: list, target: int) -> int:
    """
    implements binary search algorithm
    steps:
    for a sorted array
    - initialize 2 pointer. called left and right
    - left pointer stay at the beginning of the array (index 0) and right pointer
      will stay at end of an array (index n)
    - find the index at the middle of the 2 pointer. (0 + n)/2
    - if middle index's element is bigger than what we need, move right pointer index
      to that position.
    - if middle element is smaller than what we need, move left pointer to
      middle index + 1 position.


    Args:
        array (list): accept sorted list
        target (int): a element which index need to find

    Returns:
        -1 if target element is not present else target element's index
    """
    left = 0
    right = len(array) - 1

    while left <= right:

        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid + 1

    return -1


if __name__ == "__main__":
    ARRAY = list(range(11))
    TARGET = 5

    result = binary_search(ARRAY, TARGET)

    if result == -1:
        print(f"Element: {TARGET} is not present in the array")
    else:
        print(f"Element: {TARGET} is present at index: {result}")
