import random

def main():

  radius = eval(input("Input radius of the circle "))

  if (radius < 0):
    print("Invalid Input")
    return main()

  else:
    area = radius * radius * 3.14
    print("Area is ",area)



def sumRandom():
  #generate random numbers
  number1 = random.randint(0,9)
  number2 = random.randint(0,9)

  if number1 < number2:
    number1, number2 = number2, number1

#ask user to calculate the answer
  inputstring = ("What is {0} + {1}? ".format(number1,number2))
  answer= int(input(inputstring))

  if answer == number1 + number2:

    print ("Correct answer")

  else:
    print ("Wrong answer try again")
    return sumRandom()

sumRandom()
