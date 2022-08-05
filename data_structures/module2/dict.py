# dictionaries are a type of key:value data type
# dictionaries are created as  you see below
d1 = {"Denver":1994, "Brittanie":1998}
print(d1) # prints entire dictonary
print()

# find value for a given key
print(d1["Denver"]) # 1994

# add a key:value combo to the dictionary
d1['Granny'] = 1952
print(d1['Granny']) # 1952

# delete a key:value pair
del(d1["Denver"])
print(d1) # only contains Brittanie and Granny

# see if a dictionary contains a given value
print("Denver" in d1) # False
print("Brittanie" in d1) # True

# get all keys 
print(d1.keys()) 

# get all values
print(d1.values())
