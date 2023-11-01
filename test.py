from GraphClasses import *
from LinkedListClasses import *

def readGraphFromFile(filename):
    fileobj = open(filename, 'r')
    data = fileobj.readlines()
    fileobj.close()

    graph = DSAGraph()
    for line in data:
        splitline = line.strip().split(' ')
        for i in range(len(splitline)):
            graph.addVertex(splitline[i])
            if i != 0:
                graph.addEdge(splitline[0], splitline[i])
    return graph


keyboardGraph = readGraphFromFile('edged.al')
longPath = keyboardGraph.dfsPathFinding('B', 'C')
longPath.display()