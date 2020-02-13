#  File: TopoSort.py

#  Description: determine if a graph has a cycle and return a list for 
#               topological sort

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567

#  Course Name: CS 313E

#  Unique Number: 51345

#  Date Created: 5/3/18

#  Date Last Modified: 5/4/18


class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):

  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  def get_label_from_idx(self, idx):
    return(self.Vertices[idx].label)

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  def find_adj_and_cycle (self, v, visited_set, dict):
    nVert = len(self.Vertices)
    for i in range(len(self.Vertices)):
      print(self.Vertices[i], end=" ")
    print("Current Vertex:",v)
    print("Set of Visited:",visited_set)

    for i in range(nVert):
      print("Integer",v,i)
      if self.adjMat[self.getIndex(v)][i] > 0 and (self.Vertices[i].wasVisited()):
          print(self.Vertices[i].label)
          return "cycle"
      if self.adjMat[self.getIndex(v)][i] > 0 and not self.Vertices[i].wasVisited():
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # def hasCycle(self):

  #   for v in self.Vertices:
  #     print(v.label)
  #     if (self.cycle_help(v.label)) == True:
  #       return True
  #     print()
  #   return False

  # #receives vertex index at v
  # def cycle_help(self, v):
  #   stk = Stack()
  #   v_set = set()


  #   #mark current vertex as visited and push to stack
  #   self.Vertices[self.getIndex(v)].visited = True
  #   print("Label of First Vertex",v)
  #   v_set.add(v)
  #   v_dict[v] = []

  #   #add to set of already visited vertices
  #   stk.push(v)

  #   while not stk.isEmpty():
  #     #get adjacent vertex, function checks
  #     #if values it compares are in visited set 
  #     u = self.find_adj_and_cycle(stk.peek(), v_set, v_dict)
  #     if u == "cycle":
  #       return True
  #     if u == -1:
  #       u = stk.pop()
  #     else:
  #       self.Vertices[u].visited = True
  #       v_set.add((self.Vertices[u].label))


  #   nVert = len(self.Vertices)
  #   for i in range(nVert):
  #     self.Vertices[i].visited = True

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()

  '''
  def has_cycle_helper(self, v, v_vertex, stack):
 
    # Mark current node as v_vertex and 
    # adds to recursion stack
    v_vertex[v] = True
    stack[v] = True
    print(v_vertex[v])
    print(stack[v])
    # Recur for all neighbours
    # if any adj_v is v_vertex and in 
    # stack then graph is cyclic
    for adj_v in self.adjMat[v]:
      print(self.adjMat[v])
      print(adj_v)
      if v_vertex[adj_v] == False:
        if self.has_cycle_helper(adj_v, v_vertex, stack) == True:
          print(adj_v, v_vertex)
          return True
      elif stack[adj_v] == True:
        print(adj_v)
        return True

    # The node needs to be poped from 
    # recursion stack before function ends
    stack[v] = False
    return False
  '''
  def has_cycle_helper(self, v, v_vertex, stack):
    if stack[v] == True:
      print(v)
      return True
    if v_vertex[v] == True:
      return False
    v_vertex[v] = True
    stack[v] = True
    hasCycle = False
    for adj_v in range(len(self.Vertices)):
      if self.adjMat[v][adj_v] > 0:
        hasCycle |= self.has_cycle_helper(adj_v, v_vertex, stack)
        if hasCycle:
          print(v)
          break
    stack[v] = False
    return hasCycle
 
    # Returns true if graph is cyclic else false
  def hasCycle(self):
    v_vertex = [False] * len(self.Vertices)
    stack = [False] * len(self.Vertices)
    for node in range(len(self.Vertices)):
      if v_vertex[node] == False:
        if self.has_cycle_helper(node,v_vertex,stack) == True:
          return True
    return False

  def toposort(self):
    for v in self.Vertices:
      print(self.topo_help(self.getIndex(v)))
    

  def topo_help(self,v):

    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    #print (self.Vertices [v])
    theStack.push (v)
    topo_list = []

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
        topo_list.append(self.get_label_from_idx(u))
        #print(self.get_label_from_idx(u), end=" ")
      else:
        (self.Vertices[u]).visited = True
        #print (self.Vertices[u])
        theStack.push(u)
    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return topo_list

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./topo2-1.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  #print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    #print (city)
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  #print ("Num edges",numEdges)
  #print(cities.Vertices)
  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int  (cities.getIndex(edge[0]))
    finish = int (cities.getIndex(edge[1]))
    weight = 1

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  # print ("\nAdjacency Matric")
  # for i in range (numVertices):
  #   for j in range (numVertices):
  #     print (cities.adjMat[i][j], end = ' ')
  #   print ()
  # print ()

  # read the starting vertex for dfs and bfs
  startVertex = "m"
  #print (startVertex)
  # close file
  inFile.close()

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  #print (startIndex)

  # do depth first search
  #print ("\nDepth First Search from " + startVertex)
  #cities.dfs (startIndex)
  #print()

  #test has cycle
  print("\nDetermine if cycle exists")
  print(cities.hasCycle())

  # toposort
  print("\nPrint Topological Sort")
  cities.toposort()
  #print(topo_list)

  cities.dfs()
   
main()

