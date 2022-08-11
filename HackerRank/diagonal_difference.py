# question
'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+2+3. The right to left diagonal =3+5+9.
Their absolute difference is |15-17| = 2.
'''

# solution
def diagonalDifference(arr):
    left_diagonal = 0 # keeps track of sum of left diagonal
    right_diagonal = 0 # keeps track of sum of right diagonal
    j = len(arr)-1 # need this to last right column 
    
    for i in range(len(arr)): # go through all rows
        left_diagonal += arr[i][i] # add up left diagonal
        right_diagonal += arr[i][j] # add up right diagonal
        j -= 1 # move one column in from the last column
    
    return abs(left_diagonal-right_diagonal)