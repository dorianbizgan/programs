#  File: Day.py

#  Description:Propt user to enter day, month and year. Print out
#day of the week for that date

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number:

#  Date Created:9/21/17

#  Date Last Modified:9/21/17


def main():

  year = 0
  month = 0
  day = 0

  month_30 = [4,6,9,11]
  month_31 = [1,3,5,7,8,10,12]

  while year < 1900 or year > 2100:
    year = eval(input("Enter year: "))

  while month < 1 or month > 12:
    month = eval(input("Enter month: "))
#if this is a leap year
  if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#and the month input is february for leap year
      while day < 1 or day > 29:
        day = eval(input("Enter day: "))
    else:
      while day < 1 or day > 28:
#check to see if the day value is viable for month put
  else:
        if month in month_30:
            while day < 1 or day > 30:
                day = eval(input("Enter day: "))
#check to see if day is viable for 31 day months
        if month in month_31:
            while day < 1 or day > 31:
                day = eval(input("Enter day: "))
#change the year for the algorithm if the month is January or February
    if month == 1 or month == 2:
        year -= 1
#convert a to fit the algorithm
  a = ((month + 9) % 12) + 1
  b = day
  c = year % 100
  d = year // 100

#variables for the algorithm
  w = (13 * a - 1 ) // 5
  x = c // 4
  y = d // 4
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7

#r gives the day of the week. r = 0 represents Sunday, r = 1 represents Monday, and so on
  print(" ")
  if r == 0:
    print("The day is Sunday ")
  elif r == 1:
    print("The day is Monday ")
  elif r == 2:
    print("The day is Tuesday ")
  elif r == 3:
    print("The day is Wednesday ")
  elif r == 4:
    print("The day is Thursday")
  elif r == 5:
    print("The day is Friday ")
  elif r == 6:
    print("The day is Saturday")

  print (a,b,c,d)


main()
