'''
StackQueueclasses.py - class for Node, Stack and Queue Data structure
'''
from LinkedListClasses import *

class DSAStack():
    '''
    Stack class - inherits structure and methods from Linked List class
                  use of the insert_first() and remove_first() methods to implement a First In Last Out Stack
    '''

    def __init__(self):         # removed size and limit from Prac03 Stack class
        self.top_item = None
        self.DSAStack = DSALinkedList()         # List for the Stack
    
    def __iter__(self):
        return iter(self.DSAStack)              # Exposes Stack's iterator

    def push(self, value):
        self.DSAStack.insert_first(value)
        self.top_item = self.DSAStack.head_node
        # print(f"Adding {self.top_item.get_value()} onto the stack")

    def pop(self):
        if self.peek():
            item_to_remove = self.DSAStack.remove_first()
            self.top_item = self.DSAStack.head_node
            # print(f"Removing {item_to_remove} from the top of the stack")
            return item_to_remove
        else:
            print("This stack is empty")

    def peek(self):
        return self.DSAStack.peek_first()        
   
    def is_empty(self):
        return self.DSAStack.is_empty()           # returns True if stack is empty

class DSAQueue():
    '''
    Queue class - inherits structure and methods from Linked List class
                  use of the remove_first() and insert_last() methods to implement a First In First Out Queue
    '''
    def __init__(self):         # removed size and max size from Prac 03 Queue class
        self.head = None
        self.tail = None
        self.DSAQueue = DSALinkedList()         # List for the Queue

    def __iter__(self):
        return iter(self.DSAQueue)              # Exposes Queue's iterator

    def enqueue(self, value):
        self.DSAQueue.insert_last(value)
        self.head = self.DSAQueue.head_node
        self.tail = self.DSAQueue.tail_node
        # print(f'Adding {self.tail.get_value()} to the queue')

    def dequeue(self):
        if self.peek():
            item_to_remove = self.DSAQueue.remove_first()
            self.head = self.DSAQueue.head_node
            self.tail = self.DSAQueue.tail_node
            # print(f"Removing {item_to_remove} from the queue")
            return item_to_remove
        else:
            print("This Queue is empty")

    def peek(self):
        return self.DSAQueue.peek_first()

    def is_empty(self):
        return self.DSAQueue.is_empty()

    def display(self):
        return [node.get_value() for node in self.DSAQueue]