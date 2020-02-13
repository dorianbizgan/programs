# Dorian Bizgan
# Nov 10, 2019
# Python 3.6

def main():
    
    # this array can be filled with any values
    # can be filled with any kind of data type
    # since it's based on index
    array = ["a",2,set("b"),["c", 4]]
    print("This is our given array:", array, "\n")
    combinations = []
    power_set = []
    
    # this is a recursive function that either calls
    # itself with a 1 or a 0, and builds the combinations list
    def combination_generator(s):
        if len(s) == len(array):
            combinations.append(str(s))
            return()
        else:
            combination_generator(s + "0")
            combination_generator(s + "1")

    # calling the generator for 0 and 1 creates all the possible
    # combinations starting with a 0 and a 1
    combination_generator("0")
    combination_generator("1")
    print("These are all possible combinations",combinations)
        
    # code below goes through generated combinations and generates a set
    # based on the values that were generated. 
    
    #if the character that it's on is a 1, it will 
    # get the value for the index in the array otherwise it will
    # move onto the next character
    for combo in combinations:
        count = 0 
        temp = []
        for char in combo:
            count += 1
            #print(item)
            if char == "1":
                temp.append(array[count - 1])
        power_set.append(temp)
        
    print("\n"*2,"This is the outcoming power set for the given array using the combinations:",power_set)
    
            
main()