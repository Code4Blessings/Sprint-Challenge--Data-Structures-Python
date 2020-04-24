from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If the length of storage is zero then add to list at the head
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            # The current item now becomes the head
            self.current = self.storage.head
        # If the length of storage is less than capacity, then add to the list at tail
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        # If the length of storage is equal to the capacity, then remove the head and replace with the new item
        elif len(self.storage) == self.capacity:
            # check if self.current.next is not None, i.e node has a next value
            # if self.current.next is not None
            if self.current.next:
                # replace value of current(oldest item) with new item
                self.current.value = item
                # increment the current item to next node(new oldest item)
                self.current = self.current.next
            #  if self.current.next is None, i.e current is at end of list, no next value
            else:
                # replace value of current with new item
                self.current.value = item
                # increment the current item back to beginning of list
                self.current = self.storage.head



    def get(self):
      	        # returns all the elements in the buffer in a list in their given order
	        # should not return any None values in the list even if they are present in the ring buffer
	        # Note:  This is the only [] allowed
	        list_buffer_contents = []

	        # TODO: Your code here

	        # start at beginning of list
	        node = self.storage.head

	        while(node):  # until node = None (end of list)
	            # The append() method in python adds a single item to the existing list.
	            list_buffer_contents.append(node.value)
	            # point to next node in the list until next is None(at the end of list) at which point you exit and return list (line 58)
	            node = node.next
	        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
