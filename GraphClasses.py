'''
GraphClasses.py - Classes for DSAGraphNode and DSAGraph
Use of Linked List Data Structure from DSALinkedList to store vertices in a graph and neighbours/links in a vertex
'''
from LinkedListClasses import *
from StackQueueClasses import *

class DSAGraphNode:                 # aka DSAGraphVertex
    '''
    DSAGraphNode uses Linked List to store the adjacency list
    As it is an aggregation of the Linked List class some functionality is done using methods from Linked List class
    '''
    def __init__(self, inLabel=None):
        self.__label = inLabel                      # identifier (like a key); string data type: A, B, C ...
        self.__links = DSALinkedList()              # storing edges(string data type) in a Linked List
        self.__visited = False                        # boolean type 

    def __iter__(self):
        return iter(self.__links)

    # Accessor methods
    def getLabel(self):                             
        return self.__label

    def getVisited(self):
        return self.__visited

    def getNeighbours(self):                        # returns the neighbours stored in a Linked List
        return self.__links

    def getAdjacent(self):                          # returns neighbours stored in a list
        return [adjacent.get_value() for adjacent in self.__links]

    def toString(self):
        return f"Label: {self.__label} Links: {self.getAdjacent()}"

    def rawString(self):
        lineUp = self.__label
        for neighbour in self.__links:
            lineUp += ' '
            lineUp += neighbour.get_value()
        return lineUp
    
    def displayLinks(self):
        return [link.get_value() for link in self.__links]

    # Mutator methods
    def setLabel(self, label):
        self.__label = label
    
    def addEdge(self, vertex):                      # building a list of its' neighbours/links
        self.__links.insert_last(vertex)            # vertex is just a label of string data type

    def removeEdge(self, link):
        self.__links.remove_by_value(link)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

class DSAGraph:
    '''
    DSAGraph uses Linked List to store the "list" of graph nodes
    contains a range of accessor, mutator and helper methods where some are inherited from Linked List to maintain the Graph's integrity
    '''
    def __init__(self):
        self.__vertices = DSALinkedList()         # Instances of DSAGraphNode will be stored in a Linked List
           
    # Accessor Methods
    def hasVertex(self, label):                       
        if self.getVertex(label):
            return True

    def getVertexCount(self):                       # Get the total number of nodes in our graph
        count = 0
        for _ in self.__vertices:                   # iterate through number of vertices in graph
            count += 1
        return count

    def getEdgeCount(self):                         # get the total number of edges in our graph
        count = 0
        for vertex in self.__vertices:                  # first iterate through the vertices
            for _ in vertex.get_value():     # then iterate through the edges for each vertex
                count += 1                              # increment count with double for loop
        return int(count/2)

    def getVertex(self, label):                       # Retrieve desired node from graph
        for vertex in self.__vertices:                  # Iterate through the Linked List
            if vertex.get_value().getLabel() == label:      # to find the vertex in this graph
                return vertex.get_value()                   # It returns the instance of DSAGraphNode

    def getAdjacent(self, label):                     # Retrieve neighbouring nodes of the desired node
        for vertex in self.__vertices:                  # Iterate through the Linked List
            if vertex.get_value().getLabel() == label:
                return vertex.get_value().getAdjacent()     # returns the list of neighbouring nodes

    def isAdjacent(self, label1, label2):             # Check if two nodes are neighbours
        return label1 in self.getAdjacent(label2)

    def displayAsList(self):                        # Display all nodes and their neigbours with an adjacency list
        return [vertex.get_value().toString() for vertex in self.__vertices]

    def getVertices(self):
        return self.__vertices

    # Mutator Methods
    def addVertex(self, label):                                           # Graph Node aka Vertex
        if not self.hasVertex(label):
            self.__vertices.insert_last(DSAGraphNode(label))                  # Add an instance of Graph Node to Graph

    def addEdge(self, label1, label2):                # if undirected add in both directions
        vertex1 = self.getVertex(label1)                    # adding edges/links between vertices/graph nodes
        if label2 not in vertex1.getAdjacent():             # validate edges are non-existent
            vertex1.addEdge(label2)
        vertex2 = self.getVertex(label2)
        if label1 not in vertex2.getAdjacent():
            vertex2.addEdge(label1)

    def deleteVertex(self, label):
        vertexToDelete = self.getVertex(label)                  # retrieve the instance of DSAGraphNode
        # 1st part is removing this vertex from its neighbours adjacency list
        for adjacent in vertexToDelete.getAdjacent():           # each adjacent is a only a label (string)
            linkToDelete = self.getVertex(adjacent)             # also an instance of DSAGraphNode
            linkToDelete.removeEdge(vertexToDelete.getLabel())             
        # 2nd part is to remove this vertex from the graph
        self.__vertices.remove_by_value(vertexToDelete)         # uses method remove_by_value from LinkedList
    
    def deleteEdge(self, label1, label2):
        linkToDelete1 = self.getVertex(label1)                  # instance of DSAGraphNode
        linkToDelete2 = self.getVertex(label2)                  # instance of DSAGraphNode
        linkToDelete1.removeEdge(linkToDelete2.getLabel())
        linkToDelete2.removeEdge(linkToDelete1.getLabel())

    # additional methods
    def degree(self, vertex):                                   # returns number of edges
        count = 0
        for _ in self.getVertex(vertex):
            count += 1
        return count

    def clearAllVisited(self):                                  # Helper Method to clear all vertices
        for vertex in self.__vertices:
            vertex.get_value().clearVisited()

    def display(self):                                          # Helper Method
        for row in self.displayAsList():
            print(row)

    def displayVertices(self):                                  # 
        return [row.get_value().getLabel() for row in self.__vertices] 
    
    def bfsPathFinding(self, start, target):        # Reworked BFS Search code from COMP5005 Assignment
        if start == target:                     # returns an empty LinkedList as it doesn't need to traverse
            return None              # empty list represents 0 edges traversed
        self.clearAllVisited()                 # clear visited status of all vertices
        path = DSALinkedList()
        path.insert_first(start)                 # first vertex in the path is start parameter (string data type)
        bfs_queue = DSAQueue()
        bfs_queue.enqueue(path)                  # store into the queue the start of the path
        while bfs_queue:
            path = bfs_queue.dequeue()              # path is referencing the LinkedList pathway our queue keeps track of
            current_vertex = path.peek_last()       # the most recent neighbour discovered will be the current vertex to visit
            self.getVertex(current_vertex).setVisited()          # set vertex in graph to visited
            for neighbour in self.getAdjacent(current_vertex):   # Iterate through all neighbours(strings) of current vertex
                if not self.getVertex(neighbour).getVisited():
                    if neighbour == target:          
                        path.insert_last(neighbour)             # Add to the path the neighbour (string)
                        return path                             # returns a pathway as LinkedList (strings)
                    else:              
                        newPath = DSALinkedList()                   # reset newPath reference to a new object
                        for place in path:                          # copy over the LinkedList from path to newPath
                            newPath.insert_last(place.get_value())  
                        newPath.insert_last(neighbour)              # store this neighbour into newPath
                        bfs_queue.enqueue(newPath)                  # which is added to the queue for keeping track of the pathway taken

    def dfsPathFinding(self, start, target):
        self.clearAllVisited()
        visited = DSALinkedList()
        start_vertex = self.getVertex(start)
        return self._dfsPathFindingRec(start_vertex, target, visited)

    def _dfsPathFindingRec(self, current_vertex, target, visited):
        current_vertex.setVisited()
        visited.insert_last(current_vertex.getLabel())
        if current_vertex.getLabel() == target:
            return visited
        for neighbour in current_vertex.getAdjacent():
            if not self.getVertex(neighbour).getVisited():
                path = self._dfsPathFindingRec(self.getVertex(neighbour), target, visited)
                if path:
                    return path                       