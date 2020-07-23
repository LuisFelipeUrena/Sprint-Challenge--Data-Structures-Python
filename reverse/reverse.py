import sys
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node):
        # print the reverse value of the list
        # if the node has a next pointercd
        # if node is None or node.next_node is None:
        #     return node
        # rest = self.reverse_list(node.next_node)
        # self.head.next_node.next_node = node
        # self.head.set_next(None)
        # return rest
        # sys.setrecursionlimit(1500)
      

        if self.head is None:
            return None
        current  = self.head
        next_ = current.next_node
        if next_ is None:
            self.reverse_list(next_)    
        prev = None
        current = self.head
        while (current is not None):
                
            next_ = current.next_node
            current.next_node = prev
            prev = current
            current = next_
        self.head = prev    
