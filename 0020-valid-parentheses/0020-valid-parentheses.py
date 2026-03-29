class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            Pair = {'(': ')', '[': ']', '{': '}'}

            for c in s:
                if c in Pair:
                    stack.append(c)
                else:
                    if not stack or Pair[stack.pop()] != c:
                        return False
            return not stack



        