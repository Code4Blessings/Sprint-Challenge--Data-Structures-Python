## UPER

### Understand the Problem
1. Write the task

A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds elements to the buffer. The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

_You may not use a Python List in your implementation of the `append` method (except for the stretch goal)_

*Stretch Goal*:  Another method of implementing a ring buffer uses an array (Python List) instead of a linked list.  What are the advantages and disadvantages of using this method?  What disadvantage normally found in arrays is overcome with this arrangement?

For example:

```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
```
2. Translate what the task is asking in plain English

### Plan
- Write Pesudocode

### Execute
- Translate your code into regular code

### Reflect
- Did the code work?  If not, what's your next plan of action?