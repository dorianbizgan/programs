#  File: TestLinkedList.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
import math


class Link (object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return(str(self.data))

    def __gt__(self, other):
        return(self.data > other.data)

    def __lt__(self, other):
        return(self.data < other.data)

class LinkedList (object):

    def __init__(self):
        self.first = None
    # get number of links 
    #def get_num_links (self):

    # add an item at the beginning of the list
    def insert_first (self, item): 
        new_link = Link(item)
        new_link.next = self.first 

        self.first = new_link


    # add an item at the end of a list
    def insert_last (self, item): 
        new_link = Link(item)
        current = self.first

        if current == None:
            self.first = new_link
            return

        else:
            while current.next != None:
                current = current.next
        current.next = new_link
      
    # add an item in an ordered list in ascending order
    def insert_in_order (self, item): 
        
        new_link = Link(item)
        current = self.first

        if self.first is None:
            new_link.next = self.first
            self.first = new_link
        elif self.first.data >= new_link.data:
            new_link.next = self.first
            self.first = new_link

        else:
            while current.next is not None and current.next.data < item:
                current = current.next
            new_link.next = current.next
            current.next = new_link


        '''
        current = self.first
        previous = None
        new_link = Link(item)
    
    
        if self.first == None:
            self.first = new_link
            return


        while current != None:
            if current.data >= new_link.data:
                break
            previous = current
            print(type(current), "Current Type before next")
            current = current.next
            print(type(current), "Current Type after next")
            print(previous)
            print(current)
        if current == None:
            print("#################################",type(previous))
            previous.next = new_link

            new_link.next = None
        if current.data >= new_link.data:
            print(type(previous), "##################999####")
            previous.next = new_link
            new_link.next = current
        #if current.data >= new_link.data:
        #    temp = current
        #    new_link.next = current
        #    temp.next = new_link


        '''




    # search in an unordered list, return None if not found
    def find_unordered (self, item): 
        current = self.first

        while current != None:
            if current.data == item:
                return (current)
            else:
                current = current.next
        return None
    
    # Search in an ordered list, return None if not found
    def find_ordered (self, item): 
    
        current = self.first

        while current != None and current.data <= item:
            if current.data == item:
                return (current)
            else:
                current = current.next
        return None

    # Delete and return Link from an unordered list or None if not found

    def deleteLink(self, item):
        current = self.first
        previous = self.first 

        if current == None:
            return None
        else:
            while current.data != item:
                print(previous)
                print(current)
                previous = current
                current = current.next
            if current == None:# might break if check here if something breaks
                previous.next = None
            previous.next = current.next
            return(current)


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        output = ""
        current = self.first

        if current == None:
            return None
        else:

            while current != None:
                output += str(current)
                output += " "
                current = current.next

        return output

    def get_num_links(self):
        current = self.first
        if current == None:
            return 0
        else:
            count = 1
            while current != None:
                count += 1
                current = current.next
            return (int(count))
    
    # Copy the contents of a list and return new list
    def copy_list (self):
        new_list = LinkedList()

        current = self.first

        while current != None:
            new_list.insert_last(current)
            current = current.next 
        return (new_list)
    
    # Reverse the contents of a list and return new list
    def reverse_list (self): 
        new_list = LinkedList()
        current = self.first

        while current != None:
            new_list.insert_first(current)
            current = current.next
        return new_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list (self): 
        sorted_list = LinkedList()
        current = self.first
        while current is not None:
            sorted_list.insert_in_order(current.data)
            current = current.next
        #sorted_list.insert_in_order(50)
        return sorted_list



    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        print(self)


        current = self.first
        if current == None:
            return True

        previous = self.first
        is_sorted = True

        while current.next != None:
            if previous > current:
                is_sorted = False
            previous = current
            current = current.next

        return is_sorted

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        return self.first == None
    
    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other): 
        current_self = self.first
        current_other = other.first

        merge_list = LinkedList()
        while current_self.next != None:
            merge_list.insert_in_order(current_self.data)
            current_self = current_self.next
        while current_other.next != None:
            merge_list.insert_in_order(current_other.data)
            current_other = current_other.next
        return merge_list

    
    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        self_cur = self.first
        other_cur = other.first

        if self.get_num_links() != other.get_num_links():
            return False

        else:
            while self_cur != None:
                if(self_cur.data != other_cur.data):
                    return False
                self_cur = self_cur.next
                other_cur = other_cur.next
            return True


    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        a = []
        current = self.first
        
        while current != None:
            if current.data in a:
                self.deleteLink(current.data)
            elif current.data not in a:
                a.append(current.data)
            current = current.next
def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    last_lst = LinkedList()
    frst_lst = LinkedList()
    nrml_list = LinkedList()


    normal_list = [1,2,3,4,5]
    second_list = [4,3,2,1]

  
    for item in normal_list:
        last_lst.insert_last(item) 
        frst_lst.insert_first(item)
        nrml_list.insert_first(item)
    '''
    print("Insert Last ", last_lst)
    nrml_list.insert_last(normal_list)     #insert last test
    print("Insert First", frst_lst)     #insert first test
    print("Search Function: ",last_lst.find_unordered(11))  #find unordered test
    print("Delete Link: ",last_lst.deleteLink(1))       #delete link test
    print("Linked list after deletion: ", last_lst)
    print("Number of Links: ",last_lst.get_num_links())                #num links test
    a = last_lst.copy_list()
    print(a)

    sorted_list = last_lst.sort_list()
    print("Sorted List: ",sorted_list)
    print(sorted_list.is_sorted())
    print("merged lists", last_lst.merge_list(frst_lst))
    print(frst_lst, last_lst.get_num_links(), nrml_list.get_num_links())
    print(nrml_list.is_equal(frst_lst))
    print(nrml_list.is_equal(frst_lst))
    '''
    print(frst_lst, last_lst)
    print(frst_lst.reverse_list())
    print(last_lst.find_ordered(3))
    print(frst_lst.find_unordered(3))
    #print(frst_lst.deleteLink(2),frst_lst)
    #print(frst_lst.remove_duplicates())
    print(frst_lst.merge_list(last_lst))
    print(frst)
    print(frst_lst.copy_list())


main()
    # Test method insert_last()         √

    # Test method insert_in_order()     √

    # Test method get_num_links()       √

    # Test method find_unordered() 
    # Consider two cases - item is there, item is not there 

    # Test method find_ordered() 
    # Consider two cases - item is there, item is not there 

    # Test method deleteLink()
    # Consider two cases - item is there, item is not there 

    # Test method copy_list()

    # Test method reverse_list()

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()
