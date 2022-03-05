class Stack:
    def __init__(self, list_=[]):
        self.stack = list_

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)