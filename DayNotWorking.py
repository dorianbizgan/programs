#  File: Day.py

#  Description:Propt user to enter day, month and year. Print out
#day of the week for that date

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number:51345

#  Date Created:9/21/17

#  Date Last Modified:9/21/17

def main():
#instantiate variables
  year = 0
  month = 0
  day = 0
 #input year, loop if year not in range
  while year < 1900 or year > 2100:
    year = eval(input("Enter year: "))
#input month, loop if month not in range
  while month < 1 or month > 12:
    month = eval(input("Enter month: "))

#temporary check to make sure this works
#      print(year)
#test if month is february and leap year
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    while day < 1 or day > 29:
      day = eval(input("Enter day: "))
#input for day if month is february and isn't leap year
  if month == 12:
    while day < 1 or day > 28:
      day = eval(input("Enter day: "))
#changes month to equal a for the test conditions
#list of months that have 30 and 31 days
  month_31 = [11,1,3,5,6,8,10]
  month_30 = [2,4,7,9]

#convert month to algorithms number
  a = ((month + 9) % 12) + 1
#input day for months other than february
  if a in month_31:
    while day < 1 or day > 31:
      day = eval(input("Enter day: "))
  if a in month_30:
    while day < 1 or day > 30:
      day = eval(input("Enter day: "))
#input for day in month if month is a 31 day month
  if a in month_31:
#      print("31 month") #temporary marker for 31 day month
      while day < 1 or day >31:
        day = eval(input("Enter day: "))
#input for day in month if month is a 30 day month
  elif a in month_30:
#      print("30 month") #temporary marker for 30 day month
      while day < 1 or day > 30:
        day = eval(input("Enter day: "))

#a is instantiated at line 30 for a test case
  if a == 11 or a == 12:
    c = year //100
  else:
    c = a % 100
  b = day
  d = a // 100

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

main()
