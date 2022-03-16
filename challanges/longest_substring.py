"""
Author: Dhruvin Shah
Email: dhruvin3@gmail.com

Leetcode#03
Task: Given a string s, find the length of the longest substring without
repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.
"""

from utils import time_it


@time_it
def longest_substring(s: str) -> int:
    """this mehtod implements finding longest substring from given substring.

    Steps:
    - initialize two pointer left and right at 0. Storage variable m.
    - with right pointer get the element and check if present in m.
        - if el present in m then move left pointer accordingly and update
        m with new value of character.
        - if el not present in m then add it to the m.
    - calculate length between left and right pointet and keep updating max_len

    Complexity:
    Time: O(N)
    Space: O(N) -> since we assign the value in the map.

    Args:
        s (str): long string.

    Returns:
        maximumn length of substring with unique characters
    """
    n = len(s)
    left = 0
    right = 0
    m: dict[str, int] = {}
    max_len = 0

    while left < n and right < n:
        el = s[right]
        if el in m:
            # why we need max(left, m[el])?
            # lets take example of string abcdeafbdgcbb
            # upon going over with left and right pointer, at one
            # point we would record c @ 3(index 2 + 1). on other instances,
            # pointer would have moved and left pointer would be at e @ 5. when
            # right pointer reaches c @ 11 (index 10 + 1) we had past history
            # of c being at 3. But left pointer is already at 5. so
            # max(5, 3 + 1) we still want to continue with 5.
            left = max(left, m[el] + 1)

        m[el] = right
        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len


if __name__ == "__main__":
    STRINGS = [
        "abcabcbb",  # 3
        "bbbbb",  # 1
        "pwwkew",  # 3
        "srsrasrsr",  # 3
        "abcdeafbdgcbb",  # 7
    ]

    for STRING in STRINGS:
        LONGEST = longest_substring(STRING)
        print(f"longest substring is: {LONGEST}")
