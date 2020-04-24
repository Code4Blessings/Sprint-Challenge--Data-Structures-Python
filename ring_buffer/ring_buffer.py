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
                self.current.value = item
                # increment the current item back to beginning of list
                self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
