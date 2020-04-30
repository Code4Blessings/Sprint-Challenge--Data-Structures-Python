class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        if node == None:
            self.head = prev
        else:
            next_node = node.next_node
            node.next_node = prev
            prev = node
            node = next_node
            self.reverse_list(node, prev)
        
    # #    Make a variable called prev and set it to None.  This will define the beginning of the list

    #     prev = None
    #     # Make a variable called `current` and set it to the head.  `current` will be used to traverse through the next node
    #     current = self.head

    #     while(current):
    #         #Make sure each node that is traversed, is not overwritten--save in a variable called next_in_line
    #         next_in_line = current.next_node

    #         #Now the next node becomes the prev
    #         current.next_node = prev
    #         #Now move to the next node in the list
    #         current = next_in_line
    #     self.head = prev



        


        


      


       
        








