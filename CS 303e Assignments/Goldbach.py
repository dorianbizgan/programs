#  File: Goldbach.py

#  Description: Take in inputs, the first being 4 or greater, and the second
#               input being greater than the first, and both are even, then
#               find combinations of numbers, that equal all even numbers
#               within the range, and print out the sums that equal the
#               number being tested, ensuring both numbers being summed are
#               prime.

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567

#  Course Name: CS 303E

#  Unique Number:51345 

#  Date Created: 10/11/17

#  Date Last Modified: 10/11/17

def main():
#prime function given in class
    def is_prime(n):
        if (n == 1):
            return False
        limit = int ( n ** .5) + 1
        div = 2
        while (div < limit):
            if (n % div == 0):               
                return False
            div += 1
        return True
#inputs for the lower and upper limits, loop if inputs are invalid
    lower = int(input("Lower Limit: "))
    upper = int(input("Upper Limit: "))
    while (lower < 4) or (lower % 2 != 0) or (upper % 2 != 0) or (upper < lower):
        lower = int(input("Lower Limit: "))
        upper = int(input("Upper Limit: "))
#iterates numbers within the range, if number is even, then print out sums
    for n in range(lower, (upper + 1),2):
        print(n, end=" ")
#print out sums, checking if they're prime before printing 
        for i in range (1,((n // 2)+1)):
            if is_prime(i) and is_prime((n - i)):
                print("=",i, "+", (n-i), end=" ")
        print()

main()
        
