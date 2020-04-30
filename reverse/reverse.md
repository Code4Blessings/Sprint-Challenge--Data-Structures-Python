## UPER

### Understand the Problem
1. Write the task

Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list using recursion, *not a loop.*

...Very straight forward


### Plan
- Write Pesudocode

1->2->3->None
```
would become...
```
3->2->1->None


- Make a variable called prev and set it to None.  This will define the beginning of the list

- Make a variable called `current` and set it to the head.  `current` will be used to traverse through the next node
note: next_node is referenced in the Node class to reference the next node

- Make sure each node that is traversed, is not overwritten--save in a variable called next_in_line

- As we traverse through the linked list, each element becomes the previous

- 

### Execute
- Translate your code into regular code (See reverse.py)

### Reflect
- Did the code work?  If not, what's your next plan of action?
  
        

