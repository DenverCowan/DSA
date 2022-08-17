# EXERCISE 1 ########################################################################
'''
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
#1
monthly_expenses = [2200,2350,2600,2130,2190]
print(f'You spent ${monthly_expenses[1]-monthly_expenses[0]} more in february \n')

#2
print(f'First quarter expenses: ${monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[2]} \n')

#3
print("did I spend $2000 in any month?", 2000 in monthly_expenses, "\n")

#4
monthly_expenses.append(1980)
print("Monthly expenses for June", monthly_expenses[5], "\n")

#5
print("You got a $200 refund for an expense in April.")
monthly_expenses[3] = monthly_expenses[3] - 200
print(f'Updated Monthly Expenses: {monthly_expenses}', "\n")

# EXERCISE 2 #######################################################################
heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

''' Using this list find out
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
#1
print(len(heroes), "\n")

#2
heroes.append("black panther")
print(heroes, "\n")

#3
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(heroes, "\n")

#4
heroes[1:3] = ["doctor strange"] # starts at 1 and is up to but not including 3
print(heroes, "\n")

#5
heroes.sort() # sorts list alphebetically in place by mutating it's index but will return None
# sorted() will return a new list that has been sorted but not alter the original list
print(heroes)






