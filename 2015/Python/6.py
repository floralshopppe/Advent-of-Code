Rows = 1000
Columns = 1000
 
f = open("2015\Python\input.txt", "r")
for x in f:
  print(x)

# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Rows):    
    a = []
    # A for loop for column entries
    for column in range(Columns):   
        a.append(0)
    matrix.append(a)
 
# For printing the matrix
for row in range(Rows):
    for column in range(Columns):
        print(matrix[row][column], end=" ")
    print()

f.close()