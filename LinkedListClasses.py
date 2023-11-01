'''
LinkedListClasses.py - class for Node and Linked List Data Structures
'''


class DSAListNode():            # from COMP5008 Lecture 04 - List and Iterators: Slide 22
    '''
    Object class for instantiating each element to operate in a Linked List Data Structure
    value can be any data type
    next_node is a pointer to the next node/object in memory
    prev_node is a pointer to the previuos node in memory
    '''
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
    
    def set_next_node(self, next_node):     # assigns the memory position of the next node/object
        self.next_node = next_node
    
    def get_next_node(self):        # returns the memory position of the next node/object
        return self.next_node
    
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node
    
    def get_prev_node(self):
        return self.prev_node
    
    def get_value(self):        # returns the value of the element of this node/object
        return self.value

class DSALinkedList():          # from COMP5008 Lecture 04 - Lists and Iterators: Slide 23-25
    '''
    Object class for instantiating a Linked List Data Structure
    This is a Doubly Linked List therefore you can traverse both ways
    Possesses both head and tail pointers
    '''
    def __init__(self, head_node=None, tail_node=None):
        self.head_node = head_node
        self.tail_node = tail_node

    def __iter__(self):
        # return IteratorLinkedList(self.head_node)
        self.current_node = self.head_node
        return self

    def __next__(self):
        if self.current_node:
            next_node = self.current_node
            self.current_node = next_node.get_next_node()
            return next_node
        else:
            raise StopIteration

    def insert_first(self, newValue):
        new_head = DSAListNode(newValue)
        current_head = self.head_node

        if current_head:                    # Checks if a head node exists
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        
        self.head_node = new_head

        if not self.tail_node:              # if there is only one node in the linked list, it becomes both head and tail
            self.tail_node = new_head

    def insert_last(self, newValue):
        new_tail = DSAListNode(newValue)
        current_tail = self.tail_node

        if current_tail:                    # Checks if a tail node exists
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        
        self.tail_node = new_tail

        if not self.head_node:
            self.head_node = new_tail

    def remove_first(self):
        removed_head = self.head_node

        if not removed_head:                # if linked list is empty
            return None
        
        self.head_node = removed_head.get_next_node()       # new head node is the next node after current head

        if self.head_node:                  # New head node does not point to a previous node
            self.head_node.set_prev_node(None)
        
        if removed_head == self.tail_node:      # if there is only one node in the list, remove both head and tail pointers
            self.remove_last()
        
        return removed_head.get_value()

    def remove_last(self):
        removed_tail = self.tail_node

        if not removed_tail:            # if linked list is empty
            return None

        self.tail_node = removed_tail.get_prev_node()       # new tail is the previous node of current tail

        if self.tail_node:                  # new tail does not point to a next node
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:      # if there is only one node in the list, remove both head and tail pointers
            self.remove_first()
        
        return removed_tail.get_value()

    def remove_by_value(self, value_to_remove):
        node = self.find(value_to_remove)
        if node:                                # Check if node exists
            if node.get_value() == self.head_node.get_value():
                self.remove_first()
            elif node.get_value() == self.tail_node.get_value():
                self.remove_last()
            else:
                # Retrieve the connecting nodes
                next = node.get_next_node()
                prev = node.get_prev_node()
                # Reform their link to bypass the mid node
                next.set_prev_node(prev)
                prev.set_next_node(next)
                # We delete the mid node by having no nodes pointing to it and it poiinting to no other nodes
                node.set_next_node(None)
                node.set_prev_node(None)

    def find(self, valueToFind):
        node_to_find = None
        current_node = self.head_node

        while current_node:
            if current_node.get_value() == valueToFind:
                node_to_find = current_node
                break
            current_node = current_node.get_next_node()
        
        return node_to_find

    def peek_first(self):
        if not self.is_empty():
            return self.head_node.get_value()
        else:
            print("Cannot peek into empty Linked List")

    def peek_last(self):
        if not self.is_empty():
            return self.tail_node.get_value()
        else:
            print("Cannot peek into empty Linked List")

    def is_empty(self):
        if self.head_node == None and self.tail_node == None:
            return True

    def display(self):
        for node in self:
            print(node.get_value(), end=' ')

# class IteratorLinkedList():
#     '''
    
#     '''
#     def __init__(self, current_node):
#         self.current_node = current_node
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current_node:
#             next_node = self.current_node
#             self.current_node = next_node.get_next_node()
#             return next_node
#         else:
#             raise StopIteration

class ListError(Exception):
    pass
