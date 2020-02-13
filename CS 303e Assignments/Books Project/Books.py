#  File: Books.py

#  Description: take two books and take a frequency analysis of words
#				and compare the two authors against one another 

#  Student Name:Dorian Bizgan

#  Student UT EID:dab4567

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created:12/4/17

#  Date Last Modified: 12/5/17

word_dict = {}
def create_word_dic():
	dictionary = open("./words.txt", "r")
	for line in dictionary:
		line = line.split()
		for word in line:
			word_dict[word] = 1
	dictionary.close()
	
def parseString(st):

	stripped_book = ""
	for line in st:
		
		line = list(line)		
		x = 0
		while x <= (len(line) - 1):
			if line[x].isalpha() or line[x].isspace():
				stripped_book += line[x]
			else:
				stripped_book += " "
			x += 1
	return(stripped_book)

def getWordFreq(book):
	#create a frequency dictionary of each word in book
	book_word_dic = {}
	#print(word_dict)
	book = book.split()

	#counts frequency of words and adds to dictionary if not
	#already in the dictionary
	for word in book:
		word = word.lower()
		if str(word) in book_word_dic:
			book_word_dic[str(word)] += 1
		else:
			book_word_dic[str(word)] = 1
	return(book_word_dic)

def wordComparison(author1, author2, book1_dict, book2_dict):
	book1_words = set()
	book2_words = set()

	book1_word_count = 0
	book2_word_count = 0

	distinc1_total = 0
	distinc2_total = 0
	#converts the dictionary into a set
	for word in book1_dict:
		book1_words.add(word)
		book1_word_count += book1_dict[word]
		
	for word in book2_dict:
		book2_words.add(word)
		book2_word_count += book2_dict[word]
		
	#finds the words not shared between the two
	author1_dist = book1_words.difference(book2_words)
	author2_dist = book2_words.difference(book1_words)
	#count the total number of usese of distint words
	for word in author1_dist:
		distinc1_total += book1_dict[word]
	for word in author2_dist:
		distinc2_total += book2_dict[word]

	print(author1)
	print("Total distinct words = ", len(book1_words))
	print("Total words (inluding duplicates) =", book1_word_count)
	print("Ratio (% of total distinct words to total words) ", (len(book1_dict)/book1_word_count)*100)
	print()
	print(author2)
	print("Total distinct words = ", len(book2_words))
	print("Total words (inluding duplicates) =", book2_word_count)
	print("Ratio (% of total distinct words to total words)", (len(book2_dict)/book2_word_count)*100)
	print()
	print(author1,"used",len(author1_dist),"words that", author2,"did not use.")
	print("Relative frequency of words used by", author1, "not in common with", author2,"=", 100*(distinc1_total/book1_word_count))
	print()
	print(author2,"used",len(author2_dist),"words that", author1,"did not use.")
	print("Relative frequency of words used by", author2, "not in common with", author1,"=", 100*(distinc2_total/book2_word_count))
	print()

def main():
	#create the dictionary
	word_dict = create_word_dic()

	#ask user to input the book title
	book1 = input(str("Enter name of first book: "))
	book2 = input(str("Enter name of second book: "))
	print()

	#open books to variables
	book1 = open(book1, "r")
	book2 = open(book2, "r")

	#parsed books
	parsed_book_1 = (parseString(book1))
	parsed_book_2 = (parseString(book2))

	#close book files
	book1.close()
	book2.close()

	#entering the last name of book author
	author1 = input("Enter last name of first author: ")
	author2 = input("Enter last name of second author: ")
	print()
	
	#get the frequency of words used by the two authors
	book1_dict = getWordFreq(parsed_book_1)
	book2_dict = getWordFreq(parsed_book_2)
	
	#compare relative frequency of uncommon words used by 
	#the two authors
	wordComparison(author1, author2, book1_dict, book2_dict)
main()