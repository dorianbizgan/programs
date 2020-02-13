#  File: ISBN.py

#  Description:read ISBN numbers from a file, determine whether
#              they're valid, and write original input and 
#              validity onto an output file

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created:10/27/17

#  Date Last Modified:10/30/17
def is_valid(last_num):
    #determine if the ISBN num is valid
    if last_num % 11 == 0:
        x = "valid"
    else:
        x = "invalid"
    return x

#determine if the input is a ISBN number that can be run
def valid_input(line):
    str_line = line[0:9]
    str_last = line[-1]
   # print(str_last.isnumeric())
    #  print(str_line)
    #  print(str_last)
    if str_line.isdigit() and len(line) == 10:
        if (str_last.isalpha() and (str_last == "x" or str_last == "X")) or str_last.isnumeric():
            #     print("True")
            return True
        else:
            #     print("False")
            return False
    else:
        # print("False")
        return False

def main():

    in_file = open ("./isbn.txt", "r")
    output_file = open("./isbnOut.txt", "w")

    for line in in_file:
        stored_line = line.replace("\n", "")
        line = (line.replace("-", ""))
        line = (line.replace("\n", ""))
        #print(line)
    #    print(line)
        if valid_input(line):
            line = (list(line))
            # print(line)
            #print(line[3])
            #  valid_input(line)
            
            line.insert(0,0)
            s1 = [0]
            s2 = [0]
            x = ""
            #  print(valid_input(line)):
            
            for i in range(len(line)):
                if line[i] == "X" or line[i] == "x":
                    line[i] = "10"
            
            #determine the first partial sums
            for i in range(len(line)):
                if (i + 1) < len(line):
                    s1.append((int(line[i + 1]) + int(s1[i])))
            s1.append(0)
            #determine the second set of partial sums
            for i in range(len(s1)):
                if (i + 1) < len(s1):
                    s2.append(s1[i] + s2[i])

            #write to file ISBN num and validity
            output_information = stored_line + "  " + is_valid(s2[-1]) + "\n"

            output_file.write(output_information)
        else:
            output_information = stored_line + "  " + "invalid" + "\n"
            output_file.write(output_information)
    in_file.close()
    output_file.close()

main()
        
