"""
LeetCode #67 - Add Binary
Difficulty: Easy

Problem:
Given two binary strings a and b, return their sum as a binary string.

Examples:
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

Approach:
- Traverse both binary strings from right to left.
- Add the corresponding bits along with the carry.
- Append the resulting bit to the answer.
- Update the carry.
- Continue until both strings and the carry are fully processed.
- Reverse the collected bits to obtain the final binary string.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

where:
n = length of string a
m = length of string b
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))


if __name__ == "__main__":
    solution = Solution()

    print(solution.addBinary("11", "1"))         # "100"
    print(solution.addBinary("1010", "1011"))    # "10101"
    print(solution.addBinary("0", "0"))          # "0"
    print(solution.addBinary("1111", "1"))       # "10000"
