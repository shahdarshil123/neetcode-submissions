class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op_stack = []
        for op in operations:
            if op == '+':
                op_stack.append(op_stack[-1] + op_stack[-2])
            elif op == 'D':
                op_stack.append(2*op_stack[-1])
            elif op == 'C':
                op_stack.pop()
            else:
                op_stack.append(int(op))
        
        total = 0
        while op_stack:
            total += op_stack.pop()
        
        return total