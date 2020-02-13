#  File: CalculatePI.py

#  Description:Randomly generate numbers in a grid, and determine if it's within a circle
#              if the number is within the circle then count that as within the circle.
#              Calculate the number in the circle and out, and see how much of a difference
#              there is between math.pi and the calculated ratio

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number:51345

#  Date Created:10/14/17

#  Date Last Modified:10/16/17

import math
import random

#calculate pi with a asked number of times
def computePI ( numThrows ):
    
  trial = 0
  in_circle = 0
#while the number of times tried is less than asked continue
  while trial < numThrows:
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    if math.hypot(xPos, yPos) < 1:
          in_circle += 1
    trial += 1
  return (in_circle / numThrows) * 4

#print function that can be called for a specified number in main
def printing( n ):
    
    calculated_pi = computePI( n )
    difference = calculated_pi - math.pi
    print("num =",n," " * (11-len(str(n))),"Calculated PI =",format(calculated_pi,".6f"),\
          "  Difference =", format(difference,"+.6f"))
#print    
def main ():

  print("Computation of PI using Random Numbers \n")
  printing(100)
  printing(1000)
  printing(10000)
  printing(100000)
  printing(1000000)
  printing(10000000)
  

main()
