#I'm guessing this is a comment xd
#So instead of while true, you want to take user input for whether he/she wants the loop to continue.
continueInput = True
#prompt user to change continueInput after each iteration of loop.

while continueInput:
  print ("Input the first number you'd like to use:")
  #I don't really understand why you indented this stuff so idk.
  try:
    #I think this should be on a new line.
    numInput1 = int(input())
    continueInput = False

    # I'm starting the second input here
    secondInput = True

while secondInput:
  print("Input your second number here:")

  try:
    numInput2 = int(input())
    secondInput = False



        # I think this checks to see if the input is a integer
        # I need to make it loop somehow if it realizes its not an int
