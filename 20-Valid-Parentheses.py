class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {"]": "[", ")": "(", "}": "{"}
        for char in s:
            if char in bracket_map:
                last_elem = stack.pop() if stack else "#"  #for one char in string
                if last_elem != bracket_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack  #not stack means an empty list == valid
