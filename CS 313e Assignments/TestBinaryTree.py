#  File: TestBinaryTree.py

#  Description: create a expression tree that can be evaluated using
#               binary tree characteristics

#  Student's Name: Dorian Bizgan

#  Student's UT EID: dab4567

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created:4/13/18

#  Date Last Modified:4/13/18

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
        self.root = None

    def createTree(self, tree_list):
        
        for num in tree_list:
            self.insert(num)

    def insert(self, val):
    	#make a new temp node
        new_node = Node(val)
        
        if self.root == None:
            #print(val)
            self.root = new_node
            #print("root after making equal to new node",self.root)
            return
        else:

	        current = self.root
	        parent = self.root

	        while current != None:
	            #print(current)
	            #print(parent)
	            parent = current
	            if val < current.data:
	                current = current.lchild
	            else: 
	                current = current.rchild

	        if val < parent.data:
	            parent.lchild = new_node
	        else:
	            parent.rchild = new_node


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

    def end (self, aNode):
        if aNode.rchild == None:

            return (aNode.data)
        else:
            self.end(aNode.rchild)
        return self.end(aNode.rchild)

    def is_similar(self, other, sNode, oNode):
        #print(sNode, oNode)
        return
        if sNode == oNode == None:
        	return
        if sNode != None and oNode != None and sNode.data == oNode.data:
        	return 
        if sNode != None or oNode != None:
        	self.is_similar(other, self.root.lchild, other.root.lchild)
        	self.is_similar(other, self.root.rchild, other.root.rchild)
        #return False
def main():

	#tree lists
    a = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 9]
    beg = [5, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77, 9]
    end = [50, 30, 70, 10, 40, 60, 80, 7, 25, 38, 47, 58, 65, 77,5]
    mid = [50, 30, 70, 10, 40, 60, 5, 7, 25, 38, 47, 58, 65, 77, 9]


    #create normal tree
    tree = Tree()
    tree_copy = Tree()
    tree_beg = Tree()
    tree_mid = Tree()
    tree_end = Tree()

    tree.createTree(a)
    tree_copy.createTree(a)
    tree_beg.createTree(beg)
    tree_mid.createTree(mid)
    tree_end.createTree(end)

    

    tree.pre_order(tree.root)
    #test is_similar
    print(tree.is_similar(tree_copy, tree.root, tree_copy.root))
    print(tree.is_similar(tree_beg, tree.root, tree_beg.root))
    print(tree.is_similar(tree_mid, tree.root, tree_mid.root))
    print(tree.is_similar(tree_end, tree.root, tree_end.root))

    end_val = tree.end(tree.root)
    print(end_val)



main()