class LinkedList (object):
	def __init__ (self):
		self.first = None

  	def insertFirst (self, data):
		newLink = Link (data)
		newLink.next = self.first
		self.first = newLink

	def insertLast (self, data):
		newLink = Link (data)
		current = self.first

	if (current == None):
	  self.first = newLink
	  return

	while (current.next != None):
	  current = current.next

	current.next = newLink

  def findLink (self, data):
	current = self.first
	if (current == None):
	  return None

	while (current.data != data):
	  if (current.next == None):
		return None
	  else:
		current = current.next

	return current

  def deleteLink (self, data):
	current = self.first
	previous = self.first

	if (current == None):
	  return None

	while (current.data != data):
	  if (current.next == None):
		return None
	  else:
		previous = current
	current = current.next

	if (current == self.first):
	 	self.first = self.first.next
	else:
	 	previous.next = current.next

	return current

def main():

	test_list = linkedList()
	user_input = ""

	while (user_input != "Exit"):

		user_input = eval(input("Enter Value you want to add, type Exit to exit"))
		test_list.append(user_input)
		print(test_list)

main()




