#  File: EasterSunday.py

#  Description: Input of a year, returns the date and month of Easter

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 9/13/17

#  Date Last Modified: 9/16/17

def main():
#user input
  y = eval(input("Enter year: "))

  a = y % 19
  b = y // 100
  c = y % 100
  d = b // 4
  e = b % 4
  g = (8 * b + 13) // 25
  h = (19 * a + b - d - g + 15) % 30
  j = c // 4
  k = c % 4
  m = (a + 11 * h) // 319
  r = (2 * e + 2 * j - k - h + m + 32) % 7
  n = (h - m + 4 + 90) // 25
  p = (h - m + r + n + 19) % 32

  print (" ")
 #print out of date and month
  if (n == 3):
    print ("In",y,"Easter Sunday is on",p,"March.")

  if (n == 4):
    print("In",y,"Easter Sunday is on",p,"April.")

main()
