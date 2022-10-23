class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node: %s>" % self.data


class LinkedList:
    """"  
    Singly Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):

        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
        
        return count


    """
    The tail is the only node that doesnt point to another node
    When another none that is the last node
    Runs in O(n)
    """