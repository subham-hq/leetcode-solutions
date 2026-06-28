"""
LeetCode #20 - Valid Parentheses
Difficulty: Easy

Problem:
Given a string s containing only the characters '(', ')', '{', '}', '[',
and ']', determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding opening bracket.

Examples:
Input: s = "()"
Output: True

Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False

Input: s = "([])"
Output: True

Input: s = "([)]"
Output: False

Approach:
- Use a stack to keep track of the expected closing brackets.
- When an opening bracket is encountered, push its matching closing bracket.
- When a closing bracket is encountered:
    - If the stack is empty or the bracket does not match the expected one,
      return False.
    - Otherwise, pop the expected bracket from the stack.
- At the end, the stack should be empty for the string to be valid.

Time Complexity: O(n)
Space Complexity: O(n)

where:
n = length of the input string
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(":
                stack.append(")")

            elif char == "{":
                stack.append("}")

            elif char == "[":
                stack.append("]")

            else:
                if not stack or char != stack[-1]:
                    return False

                stack.pop()

        return not stack


if __name__ == "__main__":
    solution = Solution()

    print(solution.isValid("()"))       # True
    print(solution.isValid("()[]{}"))   # True
    print(solution.isValid("(]"))       # False
    print(solution.isValid("([])"))     # True
    print(solution.isValid("([)]"))     # False
