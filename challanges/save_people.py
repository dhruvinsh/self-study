"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Leetcode#881
Task: You are given an array people where people[i] is the weight of the ith
person, and an infinite number of boats where each boat can carry a maximum
weight of limit. Each boat carries at most two people at the same time,
provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""

from utils import time_it


@time_it
def rescue_boat(array: list[int], limit: int) -> int:
    """python to the rescue. this method implements the logics for couting
    number of boat required to save people.

    Steps:
    - first and for most we need to sort array. (well python sort is good
    enough)
    - initialize two pointer left and right to iterate over list.
    - if left + right is <= limit then yey! save them, and keep closing the
    gap.
    - if left + right is > limit then yey! just save the right person.
    Remember the list is sorted the so right is bigger. keep closing the gap
    from right.
    - if left and right are equal that means, it just last person left. get a
    single boat for single person.

    Complexity:
    Time: O(N log(N))
        here we sorted the array (merge sort for example) has time complexity
        of O(N log(N)). when we do the loop it happens for O(N) time.
    Space: O(N)
        surprised!! It happen because of sorting algorithm.

    Args:
        array (list[int]): array of integer representing people's weight.
        limit (int): max weight boat can carry.

    Returns:
        number of rescue boat required.
    """
    # python built-in method for now!
    # space complexity fo O(N) and time complexity O(N log(N))
    array.sort()

    boats = 0
    # left and right "index"
    left = 0
    right = len(array) - 1

    while left <= right:
        if left == right:
            # last person left, get the boat. and rescue mission finish.
            boats += 1
            break

        if array[left] + array[right] <= limit:
            # both person weight is less then or equal to max limit.
            left += 1
        #     right -= 1
        #     boats += 1
        # elif array[left] + array[right] > limit:
        #     # weight total is higher then limit. save the heaviest person which
        #     # is on right side.
        #     right -= 1
        #     boats += 1

        # common logic moved here
        right -= 1
        boats += 1

    return boats


if __name__ == "__main__":
    import random

    people = [3, 2, 2, 1]
    LIMIT = 3

    BOATS = rescue_boat(people, LIMIT)
    print(f"{BOATS} boat(s) required")

    people = [random.randint(5, 10) for _ in range(1000)]
    LIMIT = 12

    BOATS = rescue_boat(people, LIMIT)
    print(f"{BOATS} boat(s) required")
