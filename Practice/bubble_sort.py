def bubble_sort():
    
    # goes through an array. If the current item in the index i is
    # greater than the value of the item after it, then swap. 
    
    # continue swapping until no swaps occur
    array = [9, 8, 7, 6, 5, 4, 3 ,2, 1, 10]
    
    # set swap to true to allow while statement to begin
    swapped = True
    
    
    while swapped == True:
        swapped = False
        for i in range(0, len(array)):
            try:
                # if the item after the current is greater, swap in place
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
                else:
                    continue
            except:
                break
        print(array)
 

bubble_sort()