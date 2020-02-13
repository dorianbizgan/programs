#  File: Hailstone.py

#  Description: Take in two imputs as a range. Keep track of the number
#  of times that it takes for it to get to zero using algorithm and print out
#  the one that took the longest and which one it was.

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9 / 28 / 17

#  Date Last Modified: 9 / 29 / 17

def main():
#initialization of variables
  num_one = 0
  num_two = 0
  n = 0
  start = 0
  biggest_count = 0
  biggest_number = 1
#loop for the first and second inputs, prompting repetitive inputs if input is less than
#1 or if the second number is less than the first 
  while num_one < 1:
    num_one = int(input("Enter starting number of the range: "))
    print("")
  while num_two < 1 or num_one > num_two:
    num_two = int(input("Enter ending number of the range: "))
    print("")
#loop for the variable x, in the range between num_one and num_two (added 1
#because the range one less than the input number_
  for x in range(num_one,num_two+1):
#sets n to x so that it can be manipulated without losing the original value
    n = x
    count = 0
#if the number is not equal to 1 then run through the loop
    while n != 1:
#if the number is even run through this loop and add one to count
      if n % 2 == 0:
        n = n // 2
        count += 1
#if the number is odd run through this loop and add one to count
      elif n % 2 != 0:
        n = n * 3 + 1
        count += 1
#if the count that it ran through is greater than the one previous to it
#then replace the biggest count and biggest number to the ones that it ran
      if count >= biggest_count:
        biggest_count = count
        biggest_number = x


#once it's done running all the numbers, print out the number that had the longest
#cycle.
  print("The number", biggest_number,"has the longest cycle lenght of", biggest_count,".")




main()
