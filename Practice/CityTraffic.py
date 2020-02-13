# City Traffic Hard Coding Challenge
# Copyright Dorian Bizgan Novov 3, 2019

def main():

	class Vertex:
		def __init__(self, v):

			self.vertex = v
			self.visited = False

		def __repr__(self):
			return(str(self.vertex))


	class Graph:
		def __init__(self):
			self.graph = {}
			self.vertex_lst = []

		def __str__(self):
			temp = ""

			for key_val in self.graph:
				key = str(key_val)
				val = str(self.graph[key_val])
				temp += key + "," + val + " "
			return(temp)

		#returns the key vertex in the vertex list for the graph
		def get_vertex(self, key):
			for item in self.graph:
				if item.vertex == key:
					return(item)
			return(False)

		# searches the index of vertex's to see if one exists already
		def search_vertex_lst(self, u):
			for v in self.vertex_lst:
				#print(self.vertex_lst)
				if v.vertex == u:
					return(v)
			return(False)

		# first check to see if vertex not in vertex list
		# second check to see if vertex doesn't exist as main point
		# if vertex already exists then add to its list
		def add_vertex(self, u, v):

			# ensures that the vertex exists in the vertex list for both u and v
			if not self.search_vertex_lst(u):
				self.vertex_lst.append(Vertex(u))
			if not self.search_vertex_lst(v):
				self.vertex_lst.append(Vertex(v))

			# case 1, the key node doesn't exist so it adds it
			if not self.get_vertex(u):
				self.graph[self.search_vertex_lst(u)] = [self.search_vertex_lst(v)]
			# case 2, key node exists, and appends to its list of connecting vertex's
			else:
				self.graph[self.search_vertex_lst(u)].append(self.search_vertex_lst(v))

		def reset_visited(self):
			for v in self.vertex_lst:
				v.visited = False

		def bfs(self, s):
			traffic = 0
			s = self.get_vertex(s)
			queue = []
			queue.append(s)

			s.visited = True

			while queue:
				s = queue.pop(0)
				#print(self.graph)
				traffic += int(s.vertex)
				#print("traffic",traffic)
				#print("this is graph s", self.graph[s])
				#print("trying to print s", s)

				for v in self.graph[s]:
					#print("this is s", s,"this is v", v)
					#print(type(v.visited))
					if v.visited == False:
						#print("hello")
						#print()
						queue.append(v)
						v.visited = True
			self.reset_visited()
			return(traffic)


		def get_max_traffic(self, s):
			max_lst = []
			curr = self.graph[self.get_vertex(s)]
			for vertex in curr:
				# mark other vertex's as visited to not allow them to be visited
				for temp in curr:
					if temp.vertex != vertex.vertex:
						temp.visited = True
				max_lst.append(self.bfs(vertex.vertex) - s)
			return(max(max_lst))

	g = Graph()

	#testing get_vertex
	#print(g.get_vertex(0))
	
	
	#adding vertex's
	g.add_vertex(1,5)
	g.add_vertex(4,5)
	g.add_vertex(3,5)
	g.add_vertex(5,1)
	g.add_vertex(5,4)
	g.add_vertex(5,3)
	g.add_vertex(5,2)
	g.add_vertex(2,5)
	g.add_vertex(2,15)
	g.add_vertex(2,7)
	g.add_vertex(7,2)
	g.add_vertex(7,8)
	g.add_vertex(8,7)
	g.add_vertex(8,38)
	g.add_vertex(15,2)
	g.add_vertex(38,8)

	
	#testing bfs
	g.bfs(1)

	print(g)
	print(g.get_max_traffic(int(input())))





main()