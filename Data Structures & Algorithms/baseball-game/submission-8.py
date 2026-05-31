class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            print(stack)

            if op == "+":
                prev_1 = int(stack.pop())
                prev_2 = int(stack.pop())
                stack.extend([prev_2, prev_1, prev_1 + prev_2])
            elif op == "D":
                prev = int(stack.pop())
                stack.extend([prev, prev * 2])
            elif op == "C":
                prev = stack.pop()
            else:
                stack.append(int(op))
            
        print(stack)
        return sum(stack)

    