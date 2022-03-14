"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Task: for a given array of integers, write a funciton to move all 0's to the
end while maintaining the relative order of the other elements
+---+---+----+---+----+
| 1 | 0 | 20 | 0 | -1 |
+---+---+----+---+----+
transform above array to 
+---+----+----+---+---+
| 1 | 20 | -1 | 0 | 0 |
+---+----+----+---+---+
"""

from utils import time_it


@time_it
def move_zero(array:list[int]) -> list[int]:
    """this approach implements generic method.
    Steps:
    - initialize one pointer called j=0
    - loop over all number, if not zero then access array[j] and assign that
    number.
    - increment j by 1. And contine for the next loop.

    Complexity:
    Time: O(2*N) = O(N)
    Space: O(1)

    Args:
        array (list[int]): unsorted array of integers with 0 in it.

    Returns:
        array with non zero number at the beginning and zero at the end.
    """
    n = len(array)
    j = 0
    # move all the valid number to the front
    for num in array:
        if num != 0:
            array[j] = num
            j += 1

    # fill all the missing zeros
    for i in range(j, n):
        array[i] = 0

    return array


if __name__ == "__main__":
    import copy
    import random

    ARRAY_SIZE = 1000000

    original = [random.randrange(0, 5) for _ in range(ARRAY_SIZE)]
    # list is mutable hence we need to make copy of it
    array = copy.deepcopy(original)

    move_zero(array)
    if ARRAY_SIZE < 20:
        print(f"Old: {original}\nNew: {array}")
