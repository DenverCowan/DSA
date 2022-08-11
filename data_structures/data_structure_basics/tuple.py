# Pythons static array data type
# tuples are a fundamental data structure in Python. they can hold multiple data types
ratings = (10,9,8,7,6,5,4,3,2,1,0)
random = ('jeremiah', 29, 1.0)
print(random)
print()

# accessing a tuple. they are zero indexed. they also support negative indexing.
print(ratings[0]) #10
print()

# tuples are immutable and therefore cannot be changed, you instead need to create a
# new tuple
ratings2 = sorted(ratings) #sorted sorts them from least to greatest
print(ratings2) #0,1,2,3,4,5,6,7,8,9,10
print()

#tuples can store other tuples. I.E. nested tuples. You can have as many nested layers 
#as you want
scoreBoard = ((1,2,3,4,5),(6,7,8,9,10))
print(scoreBoard[0][0]) #1
print(scoreBoard[1][0]) # 6

#you can add tuples
combo = random + ratings
print(combo)
print()

#you can also slice tuples
print(ratings2[0:6]) 
# you must go one past the final index to get the last value in the index.
print(ratings2[6:11]) 

#you can find out the type by using the type function
print(type(random[0])) #string

# use the len() function to find out the length of a tuple or list
print(len(ratings)) #11

# you can search a tuple for a specific value as well
print(ratings.index(9)) #1
