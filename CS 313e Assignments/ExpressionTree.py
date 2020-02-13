#  File: ExpressionTree.py

#  Description: create a expression tree that can be evaluated using
#               binary tree characteristics

#  Student's Name:Dorian Bizgan

#  Student's UT EID:dab4567

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51345

#  Date Created:4/11/18

#  Date Last Modified:4/12/18

class Stack (object):
    def __init__ (self):
        self.stack = []
        
    def push (self, item):
        self.stack.insert (0, item )
        return(str(self.stack))
    
    def pop (self):
        return self.stack.pop(0)
        
    def peek (self):
        return self.stack[0]
    def isEmpty (self):
        return (len(self.stack) == 0)
        
    def __str__(self):
        copy = self

        to_pr = ""
        while not copy.isEmpty():
            to_pr += " " + str(copy.pop())

        return to_pr

class Node(object):
    #create node object
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return(str(self.data))

class Tree(object):
    def __init__(self):
        self.root = Node(None)


    def createTree(self, expr):
        
        #make a list to insert into tree
        expr = expr.split(" ")
        operators = ['+', '-', '*', '/']
        current = self.root
        stack = Stack()

        for item in expr:
            # for left parenthesis make a new node
            if item == "(":
                current.lchild = Node(None)
                stack.push(current)
                current = current.lchild
            elif item in operators:
                current.data = item
                stack.push(current)
                current.rchild = Node(None)
                current = current.rchild
            elif item != ")" and item.isdigit():
                current.data = item
                current = stack.pop()
            else:
                if not stack.isEmpty():
                    current = stack.pop()

    #helper function for evalulate
    def operate(self, a, b, c):

        if c == "+":
            return(a + b)
        if c == "-":
            return(a - b)
        if c == "/":
            return(a / b)
        if c == "*":
            return(a * b)

    #calculate the binary tree
    def evaluate (self, aNode):
        if aNode == None:
            return 0
        if aNode.lchild == None and aNode.rchild == None:
            return float(aNode.data)
        
        return self.operate(self.evaluate(aNode.lchild), self.evaluate(aNode.rchild), aNode.data)

    #operators before operands
    def pre_order(self, aNode):
        if aNode != None:
            print(aNode.data, end=" ")
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    # operators after operands
    def post_order(self, aNode):
        if aNode != None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end=" ")
def main():

    tree = Tree()
    expr = open("expression.txt","r")
    expr = expr.readline().strip("\n")
    tree.createTree(expr)

    print(expr + " = "+ str(tree.evaluate(tree.root)))
    print()
    print("Prefix Expression:",end=" ")
    tree.pre_order(tree.root)
    print()
    print()
    print("Postfix Expression:",end=" ")
    tree.post_order(tree.root)
    print()
    




main()




