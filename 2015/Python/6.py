Row = 1000
Column = 1000
 
# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()