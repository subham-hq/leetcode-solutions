"""
LeetCode #13 - Roman to Integer
Difficulty: Easy

Problem:
Roman numerals are represented by seven symbols:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Roman numerals are usually written from largest to smallest.
However, in certain cases a smaller numeral appears before a larger one,
indicating subtraction:

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900

Given a Roman numeral, convert it to an integer.

Examples:
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58

Input: s = "MCMXCIV"
Output: 1994

Approach:
- Traverse the Roman numeral from left to right.
- If the current symbol has a smaller value than the next symbol,
  subtract it from the result.
- Otherwise, add it to the result.
- Finally, add the value of the last symbol.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        num = 0

        for i in range(len(s) - 1):
            if roman_dict[s[i]] < roman_dict[s[i + 1]]:
                num -= roman_dict[s[i]]
            else:
                num += roman_dict[s[i]]

        num += roman_dict[s[-1]]

        return num


if __name__ == "__main__":
    solution = Solution()

    print(solution.romanToInt("III"))      # 3
    print(solution.romanToInt("LVIII"))    # 58
    print(solution.romanToInt("MCMXCIV"))  # 1994
