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
def is_match(char1, char2): 
    '''function to map matches to each other stored in reverse because you will later check the 
    closing paranthesis against a stack.pop()value to see if they are balanced.'''
    match_dictionary = {')':'(',  
                        '}':'{',
                        ']':'['
    }
    return match_dictionary[char1] == char2

def is_balanced(s):
    stack = Stack()
    for char in s: # iterate through the string
        if char == '(' or char =='[' or char == '{': 
            stack.push(char) # add opening paranthesis to the stack
        if char ==')' or char == ']' or char== '}':
            if stack.size()==0: # if get a closing paranthesis and have an empty stack then False
                return False
            # if closing paranthesis is not match with last item added to stack then return False
            if not is_match(char,stack.pop()): 
                return False
    return stack.size()==0 # will only return true if stack is empty at the end of the iteration.
    # time complexity is O(n) with n being the size of the string.

print(is_balanced("({[fdas]})")) #True
print(is_balanced("(]sdfhklj")) #False