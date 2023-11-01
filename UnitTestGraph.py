'''
UnitTestGraph.py - Test Harness for Graph class
                   Format based on UnitTestLinkedList which was a provided Unit Test from Prac04
'''
#*********************************************************************
#  FILE: UnitTestGraph.py
#  AUTHOR: Gabriel Sim
#  PURPOSE: Test Harness For Graph
#  LAST MOD: 11/10/2022
#  REQUIRES: GraphClasses.py - adjust import to match your code
#*********************************************************************
from GraphClasses import *

numPassed = 0
numTests = 0

graph = None 
sTestString = ""
nodeValue = None

# Test 1 - Constructor
try:
    numTests += 1
    print("Testing creation of DSAGraph()")
    graph = DSAGraph()
    if not graph.getVertices().head_node:
        numPassed += 1
        print('Passed')
except:
    print('Failed')

# Test 2 - Add Vertex
print('Testing Adding Vertices and Edges')
try:
    numTests += 1
    print("Testing addVertex()")
    graph.addVertex('A')
    graph.addVertex('B')
    graph.addVertex('C')
    graph.addVertex('D')
    numPassed += 1
    print('Passed')
except:
    print('Failed')

# Test 3 - Add Edge
try:
    numTests += 1
    print('Testing AddEdge()')
    graph.addEdge('A', 'B')
    graph.addEdge('B', 'C')
    graph.addEdge('C', 'D')
    numPassed += 1
    print('Passed')
except:
    print('Failed')

# Test 4 - Delete Edge
try:
    numTests += 1
    print('Test deleteEdge()')
    graph.deleteEdge('A', 'B')
    numPassed += 1
    print('Passed')
except:
    print('Failed')

# Test 5 - Delete Vertex
try:
    numTests += 1
    print('Testing deleteVertex()')
    graph.deleteVertex('A')
    numPassed += 1
    print('Passed')
except:
    print('Failed')

# Test 6 - Display
try:
    numTests += 1
    print('Test display()')
    graph.display()
    numPassed += 1
    print('Passed')
except:
    print('Failed')

# Test 7 - Degree
try:
    numTests += 1
    print('Test degree()')
    print(graph.degree('B'))
    numPassed += 1
    print('Passed')
except:
    print('Failed')

# Test 8 - Clear Visited of all Vertices
try:
    numTests += 1
    print('Test clearAllVisited()')
    graph.clearAllVisited()
    if not graph.getVertex('B').getVisited() and \
        not graph.getVertex('C').getVisited() and \
            not graph.getVertex('D').getVisited():
        numPassed += 1
        print('Passed')
except:
    print('Failed')

# Test 9 - Return Shortest Path using Breadth First Search
try:
    numTests += 1
    print('Testing bfsPathFinding()')
    graph.addVertex('A')
    graph.addEdge('A', 'B')
    graph.addVertex('E')
    graph.addEdge('B', 'E')
    graph.addVertex('F')
    graph.addEdge('E', 'F')
    bfsPath = graph.bfsPathFinding('A', 'F')
    count = 0
    for _ in bfsPath:
        count += 1
    print(count)
    if count == 4:
        numPassed += 1
        print('Passed')
except:
    print('Failed')

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")