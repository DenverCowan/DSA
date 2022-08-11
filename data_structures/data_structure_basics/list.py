# Pythons dynamic array data type
#Lists are very similar to tuples but they are mutable I.E. changeable
#they can contain str, float, int, other lists, and tuples
list = ['hello world!', 1.3, 10, (9,7), [1,2]]
print(list)
print()
#access is the same as tuples
print(list[0]) # 'hello world!'
print()
# you can add things to a list, whereas you would have had to create a new tuple
# which would not be a very memory efficient solution
list2 = [1,2,3,4,5]
list2.extend(['I got added', 'So did I'])
print(list2)
print()
# you can also delete elements by their index
del(list2[0])
print(list2) #now the list starts with 2 instead of 1
print()
# strings can be converted to list with the split() function
splitExample = 'hello world'.split()
print(splitExample) # ['hello', 'world']
print()
# you can also specify what to split on AKA a delimiter
splitExample2 = 'a,b,c,d,e,f,g,h'.split(',') # splits after every comma
print(splitExample2)
print()
# lists also support aliasing (where 2 variables reference one list)
# and cloning
list3 = [1,2,3]
list4 = list3
print(list4)
# with aliasing changing either list will change both since they reference the same list
list4[0] = 0
print(list4) # 0,2,3
print(list3) # also now 0,2,3
#cloning
list5 = list3[:] #clone of list 3 as 0,2,3
list5[0]=1 # list5 is now 1,2,3
print(list5) # 1,2,3
print(list3) # still 0,2,3
print()

# help() can be run on any list to get information on what all can be done
# to a list








