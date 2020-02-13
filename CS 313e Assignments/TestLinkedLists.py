#  File: TestLinkedList.py

#  Description: tests additional functionalities given to the linked lists class

#  Student Name: Uriel Buitrago

#  Student UT EID:uab62

# Partner Name: Dorian Bizgan

# Partner UT EID: dab4567

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 03/26/18

#  Date Last Modified: 03/30/18

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
class Link(object):
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.first = None

    # add an item at the beginning of the list
    def insert_first(self,data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link


    # add an item to the end of the list
    def insert_last(self, item):
        new_link = Link(item)
        current = self.first

        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next

        current.next = new_link

    # search for an item in the list
    def find_link(self, item):
        current = self.first

        if (current == None):
            return None

        while (current.data != item):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, item):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != item):
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

    # get number of links
    def get_num_links(self):
        current = self.first
        counter = 0
        if current == None:
            return 0
        else:
            while(current!= None):
                counter += 1
                current = current.next
        return counter

    # add an item in an ordered list in ascending order
    def insert_in_order(self, item):

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


    # search in an unordered list, return None if not found
    def find_unordered(self, item):
        current = self.first
        if (current == None):
            return None

        while (current.data != item):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current


    # Search in an ordered list, return None if not found
    def find_ordered(self, item):
        current = self.first
        if (current == None):
            return None

        while (current.data != item and current.data < item):
            if (current.next == None):
                return None
            else:
                current = current.next

        if current.data == item:
            return current
        else:
            return None


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        s = ''
        counter = 0
        for i in range(self.get_num_links()):
            if counter % 10 == 0 and counter >= 10:
                if current.data != None:
                    s += '\n'
                    s += str(current.data)
                    s += '  '
                else:
                    s += '\n'
                    s += '  '

            else:
                if current.data != None:
                    s += str(current.data)
                    s += '  '
                else:
                    s += '  '

            counter += 1
            current = current.next

        return s



    # Copy the contents of a list and return new list
    def copy_list(self):
        original = self.first
        copy_list = LinkedList()

        for i in range(self.get_num_links()):
            copy_list.insert_last(original.data)
            original = original.next

        return copy_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        current = self.first
        reversed_list = LinkedList()

        for i in range(self.get_num_links()):
            current = self.first
            # find the last key
            for j in range(i+1, self.get_num_links()):
                current = current.next
            # insert last key into the new list and then delete
            reversed_list.insert_last(current.data)
            self.delete_link(current)

        return reversed_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        # selection sort
        sorted_list = LinkedList()
        current_link = self.first
        #next_iter_link = self.first
        #temp = None
        if current_link == None:
            return None
        for i in range(self.get_num_links()):
            sorted_list.insert_in_order(current_link.data)
            current_link = current_link.next

        return sorted_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first

        if current == None:
            return True

        while current != None and current.next != None:
            if current.next.data < current.data:
                return False
            elif current.next.data >= current.data:
                current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        # Method: add two lists to one big linked list and then sort it
        print(self)
        print(other)
        New_Linked = LinkedList()
        current1 = self.first
        current2 = other.first

        while current1 != None:
            New_Linked.insert_in_order(current1.data)

            current1 = current1.next

        while current2 != None:
            New_Linked.insert_in_order(current2.data)

            current2 = current2.next

        return New_Linked



    # Test if two lists are equal, item by item and return True
    # same number of links and data matches in order
    def is_equal(self, other):
        self_cur = self.first
        other_cur = other.first
        if self.get_num_links() != other.get_num_links():
            return False

        else:
            while self_cur != None and other_cur != None:
                if self_cur.data != other_cur.data:
                    return False
                self_cur = self_cur.next
                other_cur = other_cur.next

            return True

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        items = []
        current = self.first
        new_list = LinkedList()

        for i in range(self.get_num_links()):
            items.append(current.data)
            current = current.next

        unique = list(set(items))

        for item in unique:
            new_list.insert_last(item)

        return new_list


def main():
    dummy = [None]
    normal_list = [1,2,4,5,6,7,9,10]
    third = [1,2,4,5,6,7,9,10]
    backwards_list = [1,10,8,9,7,5,6,4,3,2,11,12]
    linked_list = LinkedList()
    in_order_list = LinkedList()
    for item in normal_list:
        linked_list.insert_last(item)

    dummy_link = LinkedList()

    second_list = LinkedList()

    # create list that is in order by inserting nums from backwards list last
    for item in backwards_list:
        second_list.insert_last(item)
    third_link = LinkedList()
    for item in third:
        third_link.insert_last(item)

    for item in backwards_list:
        in_order_list.insert_in_order(item)

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    # NOT YET TESTED

    # Test method insert_last()
    print(color.BOLD + "Insert Last with list : 1,2,4,5,6,7,9,10" + color.END)
    print("_____________________________________")
    print(linked_list)
    print()

    # Test method insert_in_order()
    print(color.BOLD + "Insert items in order from list: 1,10,8,9,7,5,6,4,3,2,11,12" + color.END)
    print("_____________________________________")
    print(in_order_list)
    print()

    # Test method get_num_links()
    print(color.BOLD + "Test for num links" + color.END)
    print("_____________________________________")
    print("Expected output for second list = 12 \nActual                          =",second_list.get_num_links())
    print("_____________________________________")
    print("Expected output for dummy  list = 0 \nActual                          =",dummy_link.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - item is there, item is not there
    print(color.BOLD + "Find a num in a unordered list" + color.END)
    print("_____________________________________")
    print("Case 1: Item   in   list:",second_list.find_unordered(9))
    print("Case 2: Item not in list:",second_list.find_unordered(100))
    print()

    # Test method find_ordered()
    # Consider two cases - item is there, item is not there
    print(color.BOLD + "Find a item in a ordered list" + color.END)
    print("_____________________________________")
    print("Item  exists  in the  list:",linked_list.find_ordered(2))
    print("Item doesn't exist in list:",linked_list.find_ordered(3))
    print()

    # Test method delete_link()
    # Consider two cases - item is there, item is not there


    # Test method copy_list()
    print(color.BOLD + "Test Copying list: " + str(linked_list) + color.END)
    print("_____________________________________")
    new_list = linked_list.copy_list()
    print("Copy      of      list:",new_list)

    # Test method reverse_list()
    new_list = new_list.reverse_list()
    print("Reverse of copied list:",new_list)
    print()

    # Test method sort_list()
    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()
    print(color.BOLD + "Determine if a list is empty" + color.END)
    print("_____________________________________")
    print("Test List 1:", second_list)
    print(second_list.is_empty())
    print("Test List 2:", dummy_link)
    print(dummy_link.is_empty())
    print()

    # Test method merge_list()
    print(color.BOLD + "Test Merging Lists" + color.END)
    print("_____________________________________")
    merged = linked_list.merge_list(second_list)
    print("Merged list",merged)
    print()
    print("Original  List",linked_list)
    print("Copied of list",linked_list.copy_list())
    print()
    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(color.BOLD + "Determine if lists are equal" + color.END)
    print("_____________________________________")
    copy1 = linked_list.copy_list()
    print("List 1:", copy1)
    print("List 2:", linked_list)
    print("List 3:", dummy_link)
    print()
    print("Compare List 1 to list 2 \n",linked_list.is_equal(copy1))
    print("Compare List 1 to list 3 \n",linked_list.is_equal(dummy_link))
    print()


    # Test remove_duplicates()
    print(color.BOLD + "Test Remove Duplicates" + color.END)
    print("_____________________________________")
    print("Previous Merged list with duplicates:",merged)
    merged = merged.remove_duplicates()
    print("List with duplcates removed", merged)
    print()
    # delete
    while not merged.is_empty():
        merged.delete_link(merged.first.data)

    print("Merged list with all elements removed:", merged)


if __name__ == "__main__":
  main()
