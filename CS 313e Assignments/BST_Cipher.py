#  File: BST_Cipher.py

#  Description: Create key map using key string
#               Allows user to encrypt and decrypt 
#               with the respective encryption key

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 4/17/18

#  Date Last Modified: 4/18/18



import re

class Node(object):
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  def __str__(self):
    return (str(self.data))

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    chrs = []
    for word in re.split(r'(\s+)', encrypt_str.strip("\n")):
      for ch in word:
        self.insert(ch)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):

    node = Node(ch)
    if self.root == None:
      self.root = node
      return

    else:
      parent = self.root
      child = self.root

      while child != None:
        parent = child
        #if duplicate character don't reinput
        if ch == parent.data:
          return
        #if char is before current
        if ch < child.data:
          child = child.lchild
        #if char is after current
        else:
          child = child.rchild

      if ch < parent.data:
        parent.lchild = node
      else:
        parent.rchild = node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    return(self.sch_help(ch, self.root, ""))

  def sch_help(self,search,cur_node, path):
    #if current node is none means not found
    if cur_node == None:
      return ("")
    #if root is the search value
    if self.root.data == search:
      return("*!")

    #if not found and not at end
    if cur_node.data != search and cur_node != None:
      if search < cur_node.data:
        #if search value is less than current
        return(self.sch_help(search, cur_node.lchild, path + "<"))
        #if search valu eis greater than current
      else:
        return(self.sch_help(search, cur_node.rchild, path + ">"))

    return (path + "!")

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    if st == "*!":
      return self.root.data
    return(self.trav_help(st))

  def trav_help(self, path):
    current = self.root
    for direction in path:
      if direction == "<":
        current = current.lchild
      elif direction == ">":
        current = current.rchild
      else:
        return(current.data)
  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    en_k = ""
    for word in re.split(r'(\s+)', st.strip("\n")):
      for ch in word:
        en_k += self.search(ch)

    return(en_k)
  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    
    path_list = []
    for ch in st:
      path_list.append(ch)

    current = self.root
    de_k = "" 

    for direction in path_list:

      if direction == "*":
        continue
      elif direction == "!":
        de_k += current.data
        current = self.root
        continue
      elif direction == "<":
        current = current.lchild
        continue
      else:
        current = current.rchild
        continue 
    return de_k

  def in_order(self, aNode):
    #print the tree in order from least to greatest values
    if aNode != None:
      self.in_order(aNode.lchild)
      print(aNode.data, end=" ")
      self.in_order(aNode.rchild)


def main():
  a = input("Enter encryption key: ")
  print()
  crypt = Tree(a)

  en_k = input("Enter string to be encrypted: ")
  print("Encrypted string:",crypt.encrypt(en_k))
  print()
  de_k = input("Enter string to be decrypted: ")
  print("Decrypted string:",crypt.decrypt(de_k))
  print()

  #print(a.strip("\n").split())
  

  #print("Path to find character t |",crypt.search("t"))
  #print("Path to find character h |",crypt.search("h"))
  #print("Path to find character e |",crypt.search("e"))
  #print("Path to find character a |",crypt.search("a"))
  #print("Path to find character   |",crypt.search(" "))
  #print("Path to find character z |",crypt.search("z"))
  #print("===================================")
  # print("Character of path *      |",crypt.traverse("*!"))
  # print("Character of path <      |",crypt.traverse("<!"))
  # print("Character of path <<     |",crypt.traverse("<<!"))
  # print("Character of path <<<    |",crypt.traverse("<<<!"))
  # print("Character of path <>     |",crypt.traverse("<>!"))
  #print("===================================")
  #print("Sentence: meet me")
  #print("Encrypted Sentence       |",crypt.encrypt("meet me"))
  #print("Decrypted Sentence       |",crypt.decrypt("*!<!<!>!<<!*!<!"))
  #crypt.in_order(crypt.root)

main()