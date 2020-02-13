#  File: Triangle.py

#  Description: Takes a file that is a triangle finds the largest path using 4 different methods

#  Student's Name: Dorian Bizgan

#  Student's UT EID: dab4567

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 3/6/18

#  Date Last Modified: 3/9/18

import time

all_sums = [0]
new_triangle = []


# returns the greatest path sum using exhaustive search
def exhaust_helper(row, col, grid, total_sum):
  if row == len(grid):
    if total_sum > all_sums[0]:
      all_sums[0] = total_sum
    
  else:
    #print(total_sum)
    exhaust_helper(row + 1, col,     grid, int(total_sum) + int(grid[row][col]))
    exhaust_helper(row + 1, col + 1, grid, int(total_sum) + int(grid[row][col]))

def exhaustive_search (grid):
  total_sum = 0
  row = 0
  col = 0
  exhaust_helper(row, col, grid, total_sum)


# returns the greatest path sum using greedy approach
def greedy (grid):

  sum_greed = 0
  j = 0
  for i in range(len(grid)):
    if j + 1 < len(grid[i]) and grid[i][j] > grid[i][j + 1]:
      sum_greed += grid[i][j]
    elif j + 1 < len(grid[i]):
      sum_greed += grid[i][j + 1]
      j += 1
    else:
      sum_greed += grid[i][j]
  return (sum_greed)

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_helper (grid, row, col):

  if row + 1 == len(grid):

    return grid[row][col]
  else:
    if rec_helper(grid, row + 1, col) > rec_helper(grid, row + 1, col + 1):
      return grid[row][col] + rec_helper(grid, row + 1, col)
    else:
      return grid[row][col] + rec_helper(grid, row + 1, col + 1)

def rec_search (grid):
  return(rec_helper(grid, 0, 0))


def dynamic (grid):
  new_grid = dyn_helper(grid, len(grid) - 1, 0)
  #max_value = new_grid[0][0]
  #print("Grid inside the Main Dynamic Function: ", grid)
  #print(grid[0])
  return(grid[0][0], grid)
  #print("grid inside dynamic statement",type(d))
  #return (d[0][0], d);

def dyn_helper(grid, row, col):

  if len(grid[row]) == 1:
    #print("grid inside helper:", type(grid))
    #print(grid)
    return (grid)
  elif col + 1 < len(grid[row]):
    #print(col)
    if len(grid[row - 1]) >= 1 and grid[row - 1][col] + grid[row][col] > grid[row - 1][col] + grid[row][col + 1]:
      grid[row - 1][col] = grid[row - 1][col] + grid[row][col]
      dyn_helper(grid, row, col + 1)
    else:
      grid[row - 1][col] = grid[row - 1][col] + grid[row][col + 1]
      dyn_helper(grid, row, col+1)
  else:
    #print(new_triangle)
    if len(grid) > 1:
      new_triangle.append(grid[row])
      dyn_helper(grid, row - 1, 0)

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  in_file = open("triangle.txt", "r")
  len_lines = int(in_file.readline())
  in_file = in_file.readlines()
  grid = []

  for line in in_file:
    line = line.strip(" \n ")
    line = line.split(" ")

    temp_list = []
    for element in line:
      temp_list.append(int(element))

    grid.append(temp_list)
  return (len_lines,grid) 

def main():
  # read triangular grid from file

  a = read_file()
  len_lines = a[0]
  grid = a[1]
  



  ti = time.time()
  exhaustive_search(grid)
  tf = time.time()
  print("The greatest path sum through exhaustive search is " + str(max(all_sums)) + ".")
  # output greates path from exhaustive search

  
  del_t = tf - ti
  # print time taken using exhaustive search
  print("The time taken for exhaustive search is " + str(del_t) +  " seconds.")
  print()

  ti = time.time()
  # output greates path from greedy approach
  print("The greatest path sum through greedy search is " + str(greedy(grid)) + ".") 
  tf = time.time()

  del_t = tf - ti
  # print time taken using greedy approach
  print("The time taken for greedy search is " + str(del_t) + " seconds.")
  print()

  ti = time.time()
  print("The greatest path sum through recursive search is " + str(rec_search(grid)) + ".")# output greates path from divide-and-conquer approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach
  print("The time taken for recursive search is " + str(del_t) + " seconds.")
  print()
  

  ti = time.time()
  a = dynamic(grid)
  tf = time.time()
  print("The greatest path sum through dynamic search is " + str(a[0]) + ".")
  # output greates path from dynamic programming
  del_t = tf - ti
  print("The time taken for dynamic search is " + str(del_t) + " seconds.")
  

  #print(a)

  
  # print time taken using dynamic programming

  #if __name__ == "__main__":

main()