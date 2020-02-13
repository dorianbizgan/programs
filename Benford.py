#  File: Benford.py

#  Description: Takes census data, looks at the first digit of each 
#				number and adds it to its relevant freq list 

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created:11/29/17

#  Date Last Modified:11/29/17


def main():
  # create an empty dictionary
  pop_freq = {}
  count = 0
  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()

    # get the last element that is the population number
    pop_num = pop_data[-1]
    # make entries in the dictionary
    pop_freq[pop_num[0]] += 1
    count += 1
  print("{:<6}".format("Digit"), "{:<6}".format("Count"), "{:<6}".format("%"))
  for line in pop_freq:
      print("{:<6}".format(line), "{:<6}".format(pop_freq[line]), "{:<6.1f}".format((pop_freq[line]/count)* 100))
  # close the file
  in_file.close()

  # write out the result
  
main()
