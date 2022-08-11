# sets are unordered data types in python and they only contain unique 
# elements I.E. (one copy of each element)
set0 = {'hello', 'my', 'name', 'is','Denver'}
# you can typecast a list to a set and it will remove duplicates
list = ['Thriller', 'Thriller']
print(list) # ['Thriller', 'Thriller']
print()

set2 = set(list) # typecasting the list to a set
print(set2) # {'Thriller'}
print()

# set operations

# adding a element to a set
set2.add("Michael Jackson")
print(set2) # {'Michael Jackson', 'Thriller' }
print()

# removing an element
set2.remove("Thriller")
print(set2) # {'Michael Jackson'}
print()

# verify if an element is in a set
print("Michael Jackson" in set2) # True
print("Thriller" in set2) # False
print()

#Math operations on sets

# finding a union of two sets I.E. overlapping elements
set3 = {'hello World!', 'whats up', 'bye'}
set4 = {'hello World!', 'bye' }

set5 = set3 & set4 # can also use set3.intersection(set4)
print(set5) # {'hello World!','bye'}
print()

# check to see if a set is a subset of another set

print(set5.issubset(set3)) # True, because all set5 is contained in set3 as well
print()

# create a set with the contents of two other sets
set6 = set3.union(set2)
print(set6)