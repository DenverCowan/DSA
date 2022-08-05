# Quadratic running time O(n^2)
list = [5,4,3,2,1] # unordered list
def InsertionSort(list):

# we will start our comparisons at index [1]
    for elements in range(1, len(list)): # loops through [4,3,2,1], it omits the first element from comparing with itself
        j = elements # just an element to keep track of our index position in our inner loop
        while j > 0  and list[j-1] > list[j]: # while left neighbor is bigger than current element/ j > 0 avoids negative indexing
            list[j-1], list[j] = list[j], list[j-1] # swap them
            j -= 1 # decrement j to compare to the next element or if at index 0 break the while loop and move to the next index based on our outer for loop
            print(j) # unnecessary but shows how j changes with each iteration through the while loop

print(list) # original list
InsertionSort(list) # sort list
print()
print(list) # print sorted list

