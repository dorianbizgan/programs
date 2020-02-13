#  File: BabyNames.py 

#  Description:  Read file from internet, perform functions on names depending on 
#				 What user asks to be performed through input in menu

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567 

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3/19/18

#  Date Last Modified: 3/23/18


from urllib.request import urlopen
import operator

def main():
	name_dict = {}
	try:
		file = urlopen("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt") #import file from internet 
	except:
		print("Error loading file")
		return

	for line in file:
		# convert to correct format, also parsing, and converting into a list 
		line = (str(line, encoding = "utf8").strip()).split(" ")
		# convert numbers to integers and 0 values to 1001
		for k in range(len(line)):
			if line[k] == "0":
				line[k] = 1001
			elif k > 0:
				line[k] = int(line[k])

		# add the item to the dictionary, first element is the name, and the next 10 are frequencies
		name_dict[line[0]] = line[1:12]
	
	choice = 1

	while choice > 0 and choice < 7:
		choice = int(input("Options:\nEnter 1 to search for names.\nEnter 2 to display data for one name.\nEnter 3 to all names that appear in only one decade.\nEnter 4 to all names that appear in all decades.\nEnter 5 to all names that are more popular in every decade.\nEnter 6 to all names that are less popular in every decade.\nEnter 7 to quit.\nEnter a choice: "))
		print()
		if choice == 1:
			name_search = input("Enter a name ")
			in_dict(name_dict, name_search)
			print()
		if choice == 2:
			name_search = input("Enter a name ")
			print()
			single_name(name_dict, name_search)
		if choice == 3:
			decade = input("Enter a decade ")
			print("The names are first ordered by rank then alphabetically: ")
			one_decade(name_dict, decade)
		if choice == 4:
			in_all(name_dict)
		if choice == 5:
			print()
			increasing(name_dict)
		if choice == 6:
			print()
			decreasing(name_dict)
		#print(choice)
		print()
	print("Goodbye")

def in_dict(dictionary, search_name):
	try:
		count = 0
		element_num = 0

		print()
		print("The matches with their highest ranking decade are:")
		print(search_name, end=" ")
		print(dictionary[search_name].count(min(dictionary[search_name])))
		while count < dictionary[search_name].count(min(dictionary[search_name])):
			if dictionary[search_name][element_num] == min(dictionary[search_name]):
				print(str(1900 + element_num * 10), end="\n")
				count += 1
			element_num += 1
		#print(search_name + " " + str(1900 + (dictionary[search_name].index(min(dictionary[search_name])) * 10)))
		
	except KeyError:
		print()
		print("does not appear in any decade")

def single_name(dictionary, search_name):

	try:
		print(search_name, ":", end=" ")
		name_rank_list = dictionary[search_name]
		for rank in name_rank_list:
			if rank == 1001:
				rank = 0
			print(rank, end=" ")
		print()

		year = 1900
		for frequencies in dictionary[search_name]:
			if frequencies == 1001:
				frequencies = 0
			print(str(year) +  ": " +  str(frequencies))
			year += 10
	except:
		print("Sorry that person does not appear in the list")

def in_all(dictionary):
	name_count = 0
	name_list = []
	for name in dictionary:
		century = dictionary[name]

		in_all = True

		for decade in century:
			if decade == 1001:
				in_all = False
				break
		if in_all == True:
			name_list.append(name)
			name_count += 1

	print()
	print(name_count, "names appear in every decade. The names are: ")

	for name in name_list:	
		print(name)

def increasing(dictionary):

	name_count = 0
	name_list = []

	for name in dictionary:
		century = dictionary[name]
		less_than_count = 1

		for a in range(len(century) - 1):
			if century[a] > century[a + 1]:
				less_than_count += 1
		#print(less_than_count)
		if less_than_count == 11:
			name_list.append(name)
			name_count += 1
			
	print(name_count, "names are more popular in every decade:")

	for name in name_list:
		print(name)

def decreasing(dictionary):

	name_count = 0
	name_list = []

	for name in dictionary:
		century = dictionary[name]


		greater_than_count = 1

		for a in range(len(century) - 1):
			if century[a] < century[a + 1]:
				greater_than_count += 1

		if greater_than_count == 11 and 1001 not in dictionary[name]:
			name_list.append(name)
			name_count += 1			

	print(name_count, "names are less popular in every decade:")

	for name in name_list:
		print(name)

def only_one(dictionary):

	name_list = []

	for name in dictionary:
		century = dictionary[name]
		name_count = 0

		for a in range(len(century)):
			if century[a] == 1001:
				name_count += 1
		#print(less_than_count)
		if name_count == 10:
			name_list.append(name)

	print(name_count, "names in only one decade:")

	for name in name_list:
		print(name)

def one_decade (dictionary, decade):

	decade = (int(decade) % 1900) // 10
	decade_dict = {}

	for name in dictionary:
		if dictionary[name][decade] < 1001:
			decade_dict[name] = dictionary[name][decade]
	#sort dictionary, makes a tuple 
	sorted_decade_dict = sorted(decade_dict.items(), key=operator.itemgetter(1))

	# printssorted_decade_dict
	for name in sorted_decade_dict:
		print(name[0], ":", name[1])

main()