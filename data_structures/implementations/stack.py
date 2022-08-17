# a stack is a LIFO structure (last in first out)
# below is a basic implementation of a stack in python. You must import deque from collections
# to use this type of a stack
from collections import deque

class Stack:
# initializes the stack
    def __init__(self):
        self.container = deque()
# puts a value into the stack
    def push(self,value):
        self.container.append(value)
# returns and removes the last value added to the stack
    def pop(self):
        return self.container.pop()
# returns but does not remove the last value added to the stack
    def peek(self):
        return self.container[-1]
# returns true if stack is empty
    def is_empty(self):
        return len(self.container) == 0
# returns the size of the stack
    def size(self):
        return len(self.container)

# EXERCISES
# 1. reverses a string given as input using a stack
def reverse_string(s):
    stack = Stack()

    for letter in s:
        stack.push(letter)

    reversed_string = ''
    while stack.size() != 0:
        reversed_string += stack.pop()

    return reversed_string

print(reverse_string("Denver"))
print(reverse_string("victory will be mine!!!"))

'''Right idea here but had some issues because I was using append instead of the methods I 
had already created to do that for me. So, lesson here is make it easy on yourself and use the 
tools you already have available. '''

# 2. write a function that checks if parantheses are balanced or not
