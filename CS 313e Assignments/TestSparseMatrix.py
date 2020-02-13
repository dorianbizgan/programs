# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Uriel Buitrago

#  Student UT EID: uab62

#  Partner Name: Dorian Bizgan

#  Partner UT EID: dab4567

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/05/18

#  Date Last Modified: 04/08/18

class Link(object):

    def __init__(self, col=0, data=0, next=None):
        self.col = col
        self.data = data
        self.next = next

    # return a String representation of a Link (col, data)
    def __str__(self):
        s = ''
        s += '(' + str(self.col) + ',' + str(self.data) + ')'
        return s


class LinkedList(object):
    def __init__(self):
        self.first = None

    def insert_last(self, col, data):
        new_link = Link(col, data)
        current = self.first

        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next
        current.next = new_link

    def insert_link(self, col, data):

        new_link = Link(col, data)
        # print(new_link)
        current = self.first

        # if LinkedList is empty
        if current == None:
            new_link.next = current
            self.first = new_link
            return

        if current.col > new_link.col:
            new_link.next = current
            self.first = new_link
            return
        else:
            while current.next != None and current.next.col < new_link.col:
                current = current.next
            new_link.next = current.next
            current.next = new_link

    def delete_link(self, item):

        cur2 = self.first
        cur1 = self.first

        # if list is empty
        if cur1 == None:
            return None
        # if search is first item
        if cur1.data == item:
            self.first = cur1.next
        while cur2 != None and cur2.data != item:
            cur1 = cur2
            cur2 = cur2.next

        if cur2 == None:
            return None

        cur1.next = cur2.next

    # return a String representation of a LinkedList
    def __str__(self):
        s = ''
        current = self.first

        if self.first == None:

            return str(None)

        while current != None:
            if current.next != None:
                s += '{:>4}'.format(str(current)) + ' , '
            else:
                s += '{:>5}'.format(str(current))

            current = current.next

        s += '\n\n'

        return s

class Matrix(object):

    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col
        self.matrix = []

    # perform assignment operation: matrix[row][col] = data
    def set_element(self, row, col, data):
        new_link = Link(col, data)
        current = self.matrix[row].first

        while current != None and current.col != col:
            current = current.next

        if current == None:
            self.matrix[row].insert_link(col, data)
        else:
            current.data = data

    # add two sparse matrices
    def __add__(self, other):
        temp_mat = Matrix(self.col, self.row)
        
        for i in range(self.row):
            row_1 = self.get_row(i)
            row_2 = other.get_row(i)
            temp_list = LinkedList()
            
            for j in range(len(row_1)):
                temp_link = Link(row_1[j] + row_2[j])
                print(temp_link)
                temp_list.insert_last(self.col,temp_link)
            temp_mat.matrix.insert(self.row,temp_list)
            

        
        return temp_mat


    # multiply two sparse matrices
    def __mul__(self, other):

        if (self.col != other.row):
            return None
        mat = Matrix(self.row, other.col)

        for i in range(self.row):
            new_row = LinkedList()
            mat_a = self.matrix[i].first

            for j in range(other.col):
                sum_mult = 0
                for k in range(other.row):
                    first = self.get_row(i)
                    second = other.get_row(k)
                    sum_mult += first[k] * second[j]
                new_row.insert_link(j , sum_mult)
            mat.matrix.append(new_row)

        return mat


    # return a list representing a row with the zero elements inserted
    def get_row(self, n):

        if n > self.row-1:
            return None

        row = [0]*self.col
        sparsed_row = self.matrix[n].first

        for i in range(self.col):
            if sparsed_row.col == i:
                row[i] = sparsed_row.data
                if sparsed_row.next != None:
                    sparsed_row = sparsed_row.next

        return row

    # return a list representing a column with the zero elements inserted
    def get_col(self, n):

        temp_col = []

        for j in range(self.row):
            curr = self.matrix[j].first

            while curr != None and curr.col != n:
                curr = curr.next

            if curr == None:
                temp_col.append(0)


            else:
                temp_col.append(curr.data)
        return temp_col

    # return a String representation of a matrix
    def __str__(self):
        orig_mat = [[0] * self.col for _ in range(self.row)]
        s = ''
        for i in range(self.row):
            link_row = self.matrix[i].first
            while link_row != None:
                orig_mat[i][link_row.col] = link_row.data
                link_row = link_row.next

        for i in range(self.row):
            s += '\n'
            for j in range(self.col):
                s += '{:>6}'.format(orig_mat[i][j])
            s += '\n'

        return s

def read_matrix(in_file):

    line = in_file.readline().rstrip("\n").split()
    row = int(line[0])
    col = int(line[1])
    mat = Matrix(row, col)

    for i in range(row):
        line = in_file.readline().rstrip("\n").split()
        new_row = LinkedList()
        for j in range(col):
            elt = int(line[j])
            if (elt != 0):
                new_row.insert_last(j, elt)
        mat.matrix.append(new_row)
    line = in_file.readline()

    return mat


def main():
    in_file = open("Matrix.txt", "r")
    print("Test Matrix Addition")
    matA = read_matrix(in_file)
    print(matA)


    # wiping original list clean
    # global orig_cpy_mat
    # orig_cpy_mat = []

    matB = read_matrix(in_file)
    print(matB)
    matC = matA + matB
    print(matC)
    #
    print("\nTest Matrix Multiplication")
    matP = read_matrix(in_file)
    print(matP)
    matQ = read_matrix(in_file)
    print(matQ)

    print('\n Test multiplying matrices')
    matR = matP * matQ
    print(matR)

    print("\nTest Setting a Zero Element to a Non-Zero Value")
    matA.set_element(1, 1, 5)
    print(matA)

    print("\nTest Setting a Non-Zero Elements to a Zero Value")
    matB.set_element(1, 1, 0)
    print(matB)

    print("\nTest Getting a Row")
    row = matP.get_row(1)
    print(row)

    print("\nTest Getting a Column")
    col = matQ.get_col(0)
    print(col)
    print("Column Type",type(col))

    in_file.close()


main()
