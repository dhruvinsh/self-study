"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Algorithm: Sliding Window

Disscussing two different method here, one is Brute Force method (bad one) and
optimized method for that ie Sliding Window approach

Task: For given N length array, find the max sum of "k" number of consecutive
elements.
eg
arr = [1, 10, 20, 5]
k = 2
sums = [ 1+ 10, 10 + 20, 20 + 5]
sums = [11, 30, 25]
max_sum = max(sums)  # 30
"""

from typing import Union

from utils import time_it


@time_it
def brute_force(array: list[int], k: int) -> Union[int, float]:
    """brute force method to perform the given task.
    steps:
    - loop over elements from 0 to N-k
    - with initial some zero, have nested loop that would run for 0 to k
    - update max_sum form current sum and previously (assumed or detected) max
      return max out of it

    Args:
        array (list[int]): N length array
        k (int): number of consecutive elements to add

    Returns:
        maximum sum
    """
    max_sum = float("-inf")  # assume initial sum is negative infinite
    n = len(array)
    
    for i in range(0, n-k+1):
        sum = 0
        for j in range(0, k):
            sum += array[i + j]

        max_sum = max([sum, max_sum])

    return max_sum


@time_it
def sliding_window(array: list[int], k: int) -> int:

    """this function implements sliding window approach.
    it is like understand a window size of k sliding from left to right

    steps:
    - for the first k elements get the sum. and assume that is the max sum
    - loop over 0 to N-k elements. from the max sum, substract element "i"
      and add i + k element. that is new probable max sum
    - compare with previous max sum and determine new max sum and continue

    Args:
        array (list[int]): N length array
        k (int): number of consecutive elements to add

    Returns:
        maximum sum
    """
    n = len(array)
    if n <= k:
        print(f"invalid size of k {k}")
        return -1

    window_sum = sum([array[i] for i in range(k)])  # sum of the first k elements
    max_sum = window_sum  # lets assume that window sum is max sum

    for i in range(n-k):
        window_sum = window_sum - array[i] + array[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

if __name__ == "__main__":
    import random

    array = random.sample(range(0, 100000), 10000)
    k = 100

    max_sum = brute_force(array, k)
    print(f"Max Sum with brute_force method: {max_sum}\n")

    max_sum = sliding_window(array, k)
    print(f"Max Sum with sliding_window method: {max_sum}")
