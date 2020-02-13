#  File: Boxes.py

#  Description: This code finds the largest subsets of boxes that fit into each other

#  Student Name: Bosung Park

#  Student UT EID: bp24266

#  Partner Name: Nam Nguyen

#  Partner UT EID: nhn325

#  Course Name: CS 313E

#  Unique Number: 51347

#  Date Created: 2/23/2018

#  Date Last Modified: 2/24/2018

currentLongest = 0
allLists = []

def does_fit (box1, box2):
  return (box1[0] > box2[0]) and (box1[1] > box2[1]) and (box1[2] > box2[2])

def Box_recur(currIdx, currBox, resultList, boxList):

	global currentLongest
	global allLists

	if (currIdx == len(boxList) - 1):
		return resultList

	lastBox = None 
	
	if (len(resultList) > 0):
	 	lastBox = resultList[len(resultList) - 1]

	if(len(resultList) == 0 or (does_fit(currBox, lastBox))):

		dontList = Box_recur(currIdx + 1, boxList[currIdx + 1], resultList, boxList)

		tempList = list(resultList)
		tempList.append(currBox)
		appendList = Box_recur(currIdx + 1, boxList[currIdx + 1], tempList, boxList)
		
		appendLength = len(appendList)
		dontLength = len(dontList)

		if (appendLength > currentLongest):
			currentLongest = appendLength
			allLists = [appendList]
		elif (appendLength == currentLongest):
			allLists.append(appendList)

		if (dontLength > currentLongest):
			currentLongest = dontLength
			allLists = [dontList]
		elif (dontLength == currentLongest):
			allLists.append(dontList)

		if (len(appendList) >= len(dontList)):
			return appendList

		return dontList

	else:
		tempList = Box_recur(currIdx + 1, boxList[currIdx + 1], resultList, boxList)
		allLists.append(tempList)

		return tempList




def main():
	print()
	file = open("boxes.txt", "r") # open the boxes list file

	box_list = [] # list of boxes and their dimensions
	box_b = [] # empty list for boxes
	biggest_box = []

	list_length = file.readline()


	for line in file:
		line = line.strip()
		line = line.split(" ")
		line.sort()
		temporaryLine = []
		for element in line:
			temporaryLine.append(int(element))
		box_list.append(temporaryLine)
	box_list.sort() 

	if (len(box_list) == 0):
		print("Input is empty.")
		return


	out = Box_recur(0, box_list[0], [], box_list)

	idx = len(out)

	tempList = []

	for i in range (0, len(allLists)):

		if (len(allLists[i]) == idx and allLists[i] not in tempList):
			tempList.append(allLists[i])

	tempList.sort()
	if (len(tempList) == 0):
		print("No Nesting Boxes")
	elif (len(tempList) >= 2):
		print ("Largest Subset of Nesting Boxes")
		for i in range(len(tempList)):
			for j in range (len(tempList[i])):
				print (tempList[i][j])
			print ()


main()