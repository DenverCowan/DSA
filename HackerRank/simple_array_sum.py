# problem
# Given an array of integers, find the sum of its elements.

# solution
def simpleArraySum(ar):
    sum =0
    for i in ar:
        sum += i
    return sum

# Example in use
ar = [1,2,3,4,5]
print(simpleArraySum(ar)) # 15

# Time complexity is O(n), or linear because as the array grows in size the 
# algorithm grows in time.