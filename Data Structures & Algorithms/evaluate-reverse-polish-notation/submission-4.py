class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_numb = []
        for item in tokens:
            if item not in ["+", "-", "/", "*"]:
                stack_numb.append(item)
            elif item == "+":
                second = stack_numb.pop()
                first = stack_numb.pop()
                stack_numb.append(int(second) + int(first))
            elif item == "-":
                second = stack_numb.pop()
                first = stack_numb.pop()
                stack_numb.append(int(first) - int(second))
            elif item == "*":
                second = stack_numb.pop()
                first = stack_numb.pop()
                stack_numb.append(int(first) * int(second))
            elif item == "/":
                second = stack_numb.pop()
                first = stack_numb.pop()
                stack_numb.append(int(first) / int(second))
        
        return int(stack_numb[0])



        