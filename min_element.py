# -*- coding: utf-8 -*-
"""min element

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vZRsyGAKErnkzv9XAAVnuwauzEffbQa0
"""

class MinStack:
    def _init_(self):
        self.stack = []
        self.min_stack = []
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]



if _name_ == "_main_":
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.push(5)
    min_stack.push(2)
    min_stack.push(1)
    print("Minimum element after push:", min_stack.getMin())

    min_stack.pop()
    print("Minimum element after pop:", min_stack.getMin())

