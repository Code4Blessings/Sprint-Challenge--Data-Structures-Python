## UPER

### Understand the Problem

A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

2. Translate what the task is asking in plain English

- We need to build something that has a max capacity  
    - self.capacity = capacity

- While new element (item) is inserted, remove the oldest element and insert new item
    - What's the definition/structure of a queue? 
        - A queue is a data collection that follows a FIFO order
        - Therefore, if the buffer reaches max capacity, then write the structure of a queue?

### Plan
- Write Pesudocode (Accounting for what's in the test)
    - If the length of storage is zero then add to list at the head
    - If the length of storage is less than capacity, then add to the list at tail
    - If the length of storage is equal to the capacity, then remove the head and replace with the new item

### Execute
- Translate your code into regular code (See ring_buffer.py)

### Reflect
- Did the code work?  If not, what's your next plan of action?
    - First Attempt Results:
    test__array_ring_buffer (__main__.ArrayRingBufferTests) ... ERROR
test_ring_buffer (__main__.RingBufferTests) ... FAIL

Traceback (most recent call last):
  File "test_ring_buffer.py", line 49, in test__array_ring_buffer
    self.assertEqual(len(self.buffer.storage), 5)
AttributeError: 'ArrayRingBuffer' object has no attribute 'storage'

Traceback (most recent call last):
  File "test_ring_buffer.py", line 18, in test_ring_buffer
    self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd'])
AssertionError: Lists differ: [] != ['a', 'b', 'c', 'd']

Second list contains 4 additional elements.
First extra element 0:
'a'

- []
+ ['a', 'b', 'c', 'd']




