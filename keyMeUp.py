'''
keyMeUp.py - Main script for virtual keyboard program. Includes an interactive testing environment and silent mode use type
'''
import os, sys
from GraphClasses import *
from LinkedListClasses import *

def createNumSymbolsLL():
    ll = DSALinkedList()
    fileobj = open('numSymbolsList.csv', 'r')
    data = fileobj.readlines()
    fileobj.close()
    for line in data:
        
        ll.insert_last(line.strip('\n'))
    return ll

def usage():
    print(" Welcome to the Virtual Keyboard Simulation")
    print("------------------------------------------")
    print(" Usage: python3 keyMeUp.py -i")
    print("        python3 keyMeUp.py -s keyFile strFile pathFile")
    print("        where")
    print("        -i is to access Interactive Testing Environment")
    print("        -s is to run the script in silent mode")
    print("        keyFile is one of")
    print("           edged - an edged keyboard")
    print("           wrap - keyboard that wraps around edges")
    print("           switch - Nintendo Switch QWERTY keyboard with Upper Case functionality")
    print("        strFile is one of")
    print("           string1 - Quote from Shakespeare")
    print("           string2 - A sentence")
    print("           string3 - Star Wars Crawl")
    print("        pathFile is the filename(.csv) given to the paths generated from the strFile")

def printMainMenu():
    print("\n------------------------------------------\n\
Please select from the following options:\n\
1) Load keyboard file\n\
2) Vertex Operations (find, insert, delete, update)\n\
3) Edge Operations (find, add, remove, update)\n\
4) Display graph\n\
5) Display graph information\n\
6) Enter string for finding path\n\
7) Generate paths\n\
8) Display path(s) (ranked, option to save)\n\
9) Save Keyboard\n\
10) END PROGRAM")

def printSubMenuNode():
    print("Vertex Operations:\n1)Find \n2)Insert \n3)Delete \n4)Update")

def printSubMenuEdge():
    print("Edge Operations:\n1)Find \n2)Add \n3)Remove \n4)Update")

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

def readStrFromFile(filename):
    fileobj = open(filename, 'r')
    data = fileobj.readline()
    fileobj.close()
    return str(data)

def vertexOperations(graph, inChoice):
    if inChoice == '1':         # Find vertex
        vertexToFind = input("Find Vertex: ")
        vertex = graph.getVertex(str(vertexToFind).upper())
        print(vertex.toString())
    elif inChoice == '2':       # Insert vertex
        vertexToInsert = input("Insert Vertex: ")
        graph.addVertex(str(vertexToInsert).upper())
    elif inChoice == '3':       # Delete vertex
        vertexToDelete = input("Delete Vertex: ")
        graph.deleteVertex(str(vertexToDelete).upper())
    elif inChoice == '4':       # Update vertex (rename vertex label)
        rename = input("Update Vertex: ")                                   # Existing Vertex
        vertexToUpdate = graph.getVertex(str(rename).upper())                   # retrieve the instance of DSAGraphNode
        newLabel = input(f'Rename vertex {vertexToUpdate.getLabel()} into: ')       
        vertexToUpdate.setLabel(str(newLabel).upper())                              # Vertex new label
        for neighbour in vertexToUpdate.getAdjacent():                              # find adjacency list of existing vertex
            graph.getVertex(neighbour).removeEdge(rename.upper())                   # Rename label in each neighbour's adjacency list
            graph.getVertex(neighbour).addEdge(newLabel.upper())                    # with delete and add edge methods
    return graph

def edgeOperations(graph, inChoice):
    if inChoice == '1':         # Find edge
        print("Finding edge")
        edgeInput1 = input("First vertex: ")
        edgeInput2 = input("Second vertex: ")
        if graph.getVertex(edgeInput1).getNeighbours().find(edgeInput2) and graph.getVertex(edgeInput2).getNeighbours().find(edgeInput1):
            print(f"Edge {edgeInput1}{edgeInput2} exists")
    elif inChoice == '2':       # Add edge
        print("Adding Edge")
        edgeInput1 = input("First vertex: ")
        edgeInput2 = input("Second vertex: ")
        if graph.getVertex(edgeInput1) and graph.getVertex(edgeInput2):
            graph.addEdge(str(edgeInput1), str(edgeInput2))
            print(f"Vertex {edgeInput1} and {edgeInput2} are now connected.")
        else:
            print("Edges can only be added to existing vertices")
    elif inChoice == '3':       # remove edge
        print("Removing Edge")
        edgeInput1 = input("First vertex: ")
        edgeInput2 = input("Second vertex: ")
        graph.deleteEdge(edgeInput1, edgeInput2)
    elif inChoice == '4':       # update edge (relink a vertex's edge to another)
        # Uses a combination of vertex operations to achieve this
        relink = input("Update edge of Vertex: ")
        vertexToUpdate = graph.getVertex(str(relink).upper())
        edgeToUpdate = input(f'Select an existing link to relink:\n{vertexToUpdate.displayLinks()}\n: ')
        vertexToUpdate.removeEdge(str(edgeToUpdate).upper())            # remove the link from this vertex
        graph.getVertex(str(edgeToUpdate).upper()).removeEdge(str(relink).upper())      # and from the linking vertex
        edgeToCreate = input(f'Select an existing vertex to link to:\n{graph.displayVertices()}\n: ')
        graph.addEdge(str(relink).upper(), str(edgeToCreate).upper())   # add edge between the existing and user chosen vertex
    return graph

def input_to_ll(string):                               # convert our input from inbuilt python list to DSALinkedList
    LL = DSALinkedList()
    for char in string:
        if char == ' ':                                   # rename our space character to match our keyboard graph label
            LL.insert_last('SPACE')
        elif numSymbolsLL.find(char):         # 
            LL.insert_last(char)
        elif char == char.upper():                        # Add UPPER (as a vertex to travel to) if char is uppercase
            LL.insert_last('UPPER')
            LL.insert_last(char)
        else:                                             # otherwise all characters converted to uppercase to match graph labels
            LL.insert_last(char.upper())
    return LL

def validateInput(graph, ll):                         # check if all input string characters exist in our graph
    for node in ll:
        if not graph.getVertex(node.get_value()):
            return False
    return True

def cleanPathway(pathway):                              # pass in the linked list of linked lists
    cleanedPath = DSALinkedList()
    for ll in pathway:                                  # Iterate through collection of pathways
        for node in ll.get_value():                     # Iterate through each pathway
            if node.get_next_node():                    # Insert all nodes except the last one to avoid repetition
                cleanedPath.insert_last(node.get_value())           
    cleanedPath.insert_last(pathway.tail_node.get_value().tail_node.get_value())   # Insert the very last node missed by the iterations
    return cleanedPath                                  # pack cleaned pathway into a LinkedList

def countEdges(pathway):                # counts total number of edges in pathway
    count = 0
    for node in pathway:        # As the pathway sent in is cleaned
        count +=1               # We count the number of vertices
    count -= 1                  # decrement 1 to represent the number of edges
    return count
    
def savePathway(ll, writeName):
    filename = str(writeName) + '.csv'
    fileobj = open(filename, 'w')
    for node in ll:
        fileobj.write(str(node.get_value()) + ' ')
    fileobj.close()

def saveKeyboardAsFile(graph, writeName):
    filename = str(writeName) + '.al'
    fileobj = open(filename, 'w')
    for vertex in graph.getVertices():
        fileobj.write(str(vertex.get_value().rawString()) + '\n')

    fileobj.close()

# Global Data
numSymbolsLL = createNumSymbolsLL()

def main():
    printMainMenu()
    choiceMainMenu = input(": ")

    while choiceMainMenu != '10':
        if choiceMainMenu == '1':               # Type in .al filename to read into Graph
            print('Select an al file to load as Virtual Keyboard: ')
            for file in os.listdir(os.curdir):
                if file.endswith('.al'):
                    print(file)
            loadChoice = input('Type in the name of the file: ')
            keyboardGraph = readGraphFromFile(loadChoice)
            if keyboardGraph:
                print(f'{loadChoice} has been loaded as the Virtual Keyboard')
            else:
                print("No Keyboard layout detected!")
        elif choiceMainMenu == '2':             # Vertex Operations
            printSubMenuNode()
            subMenuChoice = input(": ")
            if subMenuChoice in ['1','2','3','4']:
                keyboardGraph = vertexOperations(keyboardGraph, subMenuChoice)
            else:
                print("Invalid Choice")
        elif choiceMainMenu == '3':             # Edge Operations
            printSubMenuEdge()
            subMenuChoice = input(": ")
            if subMenuChoice in ['1','2','3','4']:
                keyboardGraph = edgeOperations(keyboardGraph, subMenuChoice)
            else:
                print("Invalid Choice")
        elif choiceMainMenu == '4':              # Display as Adjacency List
            for row in keyboardGraph.displayAsList():
                print(row)
        elif choiceMainMenu == '5':             # Display graph information (the number of edges and vertices in a graph)
            print(f"Graph Vertex count: {keyboardGraph.getVertexCount()}")
            print(f"Graph Edge Count: {keyboardGraph.getEdgeCount()}")
        elif choiceMainMenu == '6':             # Store input string for path searching
            inputString = input("Enter the string: ")           
            convertedInput = input_to_ll(str(inputString))               # prepare our input for use in graph search
            convertedInput.display()
        elif choiceMainMenu == '7':             # Execute the BFS (and DFS) pathfinding algorithm
            print("Generating paths on virtual keyboard")
            optimalPath = DSALinkedList()
            if validateInput(keyboardGraph, convertedInput):        # validate if all characters exist in our keyboard
                for node in convertedInput:
                    if node.get_next_node():          # if next node exists
                        current = keyboardGraph.bfsPathFinding(node.get_value(), node.get_next_node().get_value())
                    if current:                                     # if a pathway can be generated
                        optimalPath.insert_last(current)               # add to our optimal path
                    current = None
            else:
                print("Input contains characters that are not in keyboard")

        elif choiceMainMenu == '8':             # Display the list of different paths generated (in order of shortest to longest)
            path_clean = cleanPathway(optimalPath)
            print('Converted String: ', end='')
            convertedInput.display()
            print('\nPath: ', end='')
            path_clean.display()
            print('\nVertices traversed: ', countEdges(path_clean))
            saveChoice = input('Save pathway (Y/N)?: ')
            if str(saveChoice).upper() == 'Y':
                saveName = inputString
                savePathway(path_clean, saveName)

        elif choiceMainMenu == '9':                 # Save keyboard layout to a .al file
            print("Saving keyboard layout to .al file")
            userSaveLayout = input("Save keyboard as: ")
            saveKeyboardAsFile(keyboardGraph, userSaveLayout)
        else:
            print("---------------------------------\n\tInvalid selection\n---------------------------------\n")
        printMainMenu()
        choiceMainMenu = input(": ")

if len(sys.argv) < 2:
    usage()
else:
    useType = str(sys.argv[1])

    if useType == '-i':
        main()
    elif useType == '-s':
        print('Silent Mode')
        # capture the arguments from command line
        keyFile = str(sys.argv[2]) + '.al'
        strFile = str(sys.argv[3]) + '.csv'
        pathFile = str(sys.argv[4])

        # read keyboard file
        keyboardGraph = readGraphFromFile(keyFile)
        if keyboardGraph:
            print(f'{keyFile} has been loaded as the Virtual Keyboard')
        else:
            print("Invalid keyFile input")
            sys.exit()

        # read string input
        readString = readStrFromFile(strFile)
        print('String input: ', readString)
        convertedInput = input_to_ll(readString)
        if convertedInput.head_node:
            print('Converted Input: ', end='')
            convertedInput.display()
        else:
            print("Invalid strFile input")
            sys.exit()
        
        # Generate pathways and save to csv
        print("\nGenerating paths on virtual keyboard")
        optimalPath = DSALinkedList()
        if validateInput(keyboardGraph, convertedInput):        # validate if all characters exist in our keyboard
            for node in convertedInput:
                if node.get_next_node():          # if next node exists
                    current = keyboardGraph.bfsPathFinding(node.get_value(), node.get_next_node().get_value())
                if current:                                     # if a pathway can be generated
                    optimalPath.insert_last(current)               # add to our optimal path
                current = None
        else:
            print("Input contains characters that are not in keyboard")
        
        path_clean = cleanPathway(optimalPath)
        path_clean.display()  
        print('\nOptimal Pathway: ', countEdges(path_clean))
        savePathway(path_clean, pathFile)