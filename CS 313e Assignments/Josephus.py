#  File: Josephus.py

#  Description: Circular linked list to solve josephus problem

#  Student Name: Uriel Buitrago

#  Student UT EID: uab62

#  Partner Name: Dorian Bizgan

#  Partner UT EID: dab4567

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 4/1/18

#  Date Last Modified: 4/2/18

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self == None:
            return str(None)
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, item):

        New = Link(item)
        current = self.first

        if current == None:
            self.first = New
            New.next = self.first
            return

        while (current.next != self.first):
            # print(current)
            current = current.next

        current.next = New
        New.next = self.first

    # Find the link with the given key (value)
    def find(self, key):

        current = self.first
        if current == None:
            return None
        if current.data == key:
            return current
        current = current.next

        while current != self.first:
            if current.data == key:
                return current
            current = current.next


    # Delete a link with a given key (value)
    def delete(self, key):

        if self.first == None:
            return None
        pointer_1 = self.first
        goal = self.find(key)

        if pointer_1.next.data == pointer_1.data:
            self.first = None

        elif pointer_1.data == goal.data:
            self.first = pointer_1.next
            while pointer_1.next.data != goal.data:
                pointer_1 = pointer_1.next
            pointer_1.next = self.first

        else:
            while pointer_1.next.data != goal.data:
                pointer_1 = pointer_1.next

            pointer_1.next = goal.next
        return goal


    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        if self.first == None:
            return None
        link = self.find(start)
        for i in range(n - 1):
            link = link.next
        #print('s',link, 'A',link.next)
        return self.delete(link.data).next

    # get number of links

    def get_num_links(self):
        current = self.first
        counter = 1
        current = current.next
        if current == self.first:
            return counter
        else:
            while (current != self.first):
                counter += 1
                current = current.next
        return counter

    # Return a string representation of a Circular List
    def __str__(self):
        if self.first == None:
            return str(None)
        current = self.first
        counter = 1
        string = str(current)
        string += "  "
        current = current.next
        while current != self.first:
            if counter % 10 == 0:
                string += "\n"
            if current == None:
                string += "None"
            else:

                string += str(current) + "  "
            current = current.next

            counter += 1
        return string


def main():
    in_file = open('josephus.txt', 'r')
    army_size = int(in_file.readline().strip('\n'))
    start = int(in_file.readline().strip('\n'))
    step = int(in_file.readline().strip('\n'))

    # create army
    soldiers = []

    for i in range(army_size):
        soldiers.append(i + 1)

    # create circular linked list
    Army = CircularList()

    for soldier in soldiers:
        Army.insert(soldier)

    if Army.get_num_links() == 1:
        print(Army.first.data)
        return

    print(type(step))
    to_print = Army.find(step)
    print(to_print)

    start = Army.delete_after(start,step)
    find_dead = start.data % 40


    while Army.get_num_links() > 0:
        temp = start
        for i in range(step - 1):
            temp = temp.next
        print(temp)
        
        start = Army.delete_after(int(start.data), step)
        if Army.first == None:
            break




main()
