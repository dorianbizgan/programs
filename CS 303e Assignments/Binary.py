def main():
    array = []
    for i in range (101):
        array.append(i)
    print(array)

    low = 0
    high = len(array) - 1
    search = eval(input("Enter the number you want to search: "))
    while low <= high and search <= len(array) and search >= 0:
        middle = ((high + low) // 2)  + 1
        print(middle)
        if search > array[middle]:
            low = middle
        if search < middle:
            high = middle
        if search == middle:
            print( middle)
            break

main()
