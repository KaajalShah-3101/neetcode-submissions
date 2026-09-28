class Solution:
    def isValid(self, s: str) -> bool:
        hash_map_parenthesis = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for bracket in s:
            if bracket in hash_map_parenthesis:
                if not stack:
                    return False
                first_element = stack.pop()
                if first_element != hash_map_parenthesis[bracket]:
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
        else:
            return True