'''
  File: MagicSquare.py

  Description: makes a magic square and determines if it's correct

  Student's Name: Dorian Bizgan

  Student's UT EID: dab4567

  Partner's Name:

  Partner's UT EID:

  Course Name: CS 313E

  Unique Number:51340

  Date Created: 1/25/18

  Date Last Modified: 1/26/18
'''


def make_square(dimension):
  magic_square = []
  for i in range(dimension):
    magic_square.append([])
    for j in range(dimension):
      magic_square[i].append([])

  #creating starting point and placing first num


  x = (dimension // 2)
  y = dimension - 1

  magic_square[y][x] = 1

  for k in range(2,(dimension ** 2 + 1)):
 #   print("dim", dimension, "dim sq", (dimension ** 2))

    y += 1
    x += 1

    if y > dimension - 1:
      y = 0
    if x > dimension - 1:
      x = 0
    if magic_square[y][x] != []:
      y -= 2
      x -= 1

    magic_square[y][x] = k

    #print("Current Y",y,"Current X", x)

  return(magic_square)

def print_square(magic_square):
  for i in range(len(magic_square)):
    line = ""

    for j in range(len(magic_square)):
      line += ("{:>3}".format(magic_square[i][j]))
    print(line[1:len(line)])

def check_square(magic_square, dimension):

  actual_row = 0
  actual_col = 0
  diagLR = 0
  diagRL = 0

  #checking the sums of columns and rows
  for i in range(len(magic_square)):
    row_tot = 0
    col_tot = 0
    row_tot = sum(magic_square[i])
    for j in range(len(magic_square)):
      col_tot += magic_square[i][j]
    if row_tot != dimension * (dimension ** 2 + 1) / 2:
      actual_row = row_tot
    elif i == dimension - 1:
      actual_row = row_tot
    if col_tot != dimension * (dimension ** 2 + 1) / 2:
      actual_col = col_tot
    elif i == dimension - 1:
      actual_col = col_tot

  #taking the sum of the diagonal left to right
  for i in range(len(magic_square)):
    diagLR += magic_square[i][i]

  for i in range(len(magic_square)):
    diagRL += magic_square[i][(len(magic_square) - 1) - i]


  return(actual_row, actual_col, diagLR, diagRL)



def main():


  # Prompt the user to enter an odd number 3 or greater
  dimension = eval(input("Please enter an odd number: "))
  print()

  #Checking user input
  while not dimension >= 3 or dimension % 2 == 0:
      dimension = eval(input("Please enter an odd number:"))
      print()

  # Create the magic square
  magic_square = (make_square(dimension))

  # Print the magic square
  print("Here is a", dimension, "x", dimension, "magic square:")
  print()
  print_square(magic_square)

  # Verify that it is a magic square
  row,col, diagLR, diagRL = check_square(magic_square, dimension)

  print()
  print("Sum of row = ",row)
  print("Sum of column = ",col)
  print("Sum diagonal (UL to LR) = ", diagLR)
  print("Sum diagonal (UR to LL) = ", diagRL)

main()