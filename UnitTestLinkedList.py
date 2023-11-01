'''
UnitTestLinkedList.py - Test Harness for Linked List class
                        Unit Test sourced from Blackboard under COMP5008: Prac 04 Linked Lists
'''
#*********************************************************************
#  FILE: UnitTestLinkedList.py
#  AUTHOR: Gabriel Sim (reusing all original tests (1-9)
#                       addtional tests for  other features)
#  PURPOSE: Extended Test Harness For Linked List
#  LAST MOD: 11/10/2022
#  REQUIRES: LinkedListClasses.py - adjust import to match your code
#*********************************************************************
from LinkedListClasses import * 

numPassed = 0
numTests = 0

ll = None 
sTestString = ""
nodeValue = None

#Test 1 - Constructor
print("\n\nTesting Normal Conditions - Constructor")
print("=======================================")
try:
    numTests += 1
    ll = DSALinkedList()
    print("Testing creation of DSALinkedList (isEmpty()):")
    if (not ll.is_empty()):
        raise ListError("Head must be None.")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

     
#Test 2 - Insert First
print("\nTest insert first and remove first - stack behaviour")
print("=======================================")
try:
    numTests += 1
    print("Testing insertFirst():")
    ll.insert_first("abc")
    ll.insert_first("jkl")
    ll.insert_first("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 3 - Peek First
try:
    numTests += 1
    print("Testing peek.First():")
    testString = ll.peek_first()
    if testString != "xyz":
        raise ListError("Peek First failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 4 - Remove first
try:
    numTests += 1
    print("Testing removeFirst():")
    testString = ll.remove_first()
    if testString != "xyz":
        raise ListError("Remove first failed")
    testString = ll.remove_first()
    if testString != "jkl":
        raise ListError("Remove first failed")
    testString = ll.remove_first()
    if testString != "abc":
        raise ListError("Remove first failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 5 - Remove from empty list
try:
    numTests += 1
    print("Testing removeFirst() when empty")
    testString = ll.remove_first()
    raise ListError("Remove first when empty failed")
    print("Failed")
except:
    numPassed += 1
    print("Passed")


#Test 6 - Insert Last 
print("\nTest insert last and remove first - queue behaviour")
print("=======================================")
try:
    numTests += 1
    print("Testing insertLast():")
    ll.insert_last("abc")
    ll.insert_last("jkl")
    ll.insert_last("xyz")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 7 - Peek Last
try:
    numTests += 1
    print("Testing peekFirst():")
    testString = ll.peek_first()
    if testString != "abc":
        raise ListError("Peek First failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 8 - Remove first
try:
    numTests += 1
    print("Testing removeFirst():")
    testString = ll.remove_first()
    if testString != "abc":
        raise ListError("Remove first failed")
    testString = ll.remove_first()
    if testString != "jkl":
        raise ListError("Remove first failed")
    testString = ll.remove_first()
    if testString != "xyz":
        raise ListError("Remove first failed")
    numPassed += 1
    print("Passed")
except:
    print("Failed")

#Test 9 - Is Empty
try:
    numTests += 1
    print("Testing isEmpty when empty")
    testString = ll.remove_first()
    raise ListError("Remove first when empty failed")
    print("Failed")
except:
    numPassed += 1
    print("Passed")

# Test 10 - Remove by value
try:
    numTests += 1
    print("Testing remove_by_value()")
    ll.insert_last("No")
    ll.insert_last("I")
    ll.insert_last("am")
    ll.insert_last("your")
    ll.insert_last("father")
    ll.remove_by_value('No')
    numPassed += 1
    print('Passed')
except:
    print("Failed")

# Test 11 - Find
try:
    numTests += 1
    print('Testing find()')
    node_to_find = ll.find('am')
    if node_to_find.get_value() == 'am':
        print('Passed')
        numPassed += 1
except:
    print("Failed")

# Test 12 - Display
try:
    numTests += 1
    print('Testing display()')
    ll.display()
    numPassed += 1
    print('\nPassed')
except:
    print("Failed")

# Print test summary
print("\nNumber PASSED: ", numPassed, "/", numTests)
print("-> ", numPassed/numTests*100, "%\n")
