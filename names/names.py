# importing time library to track time
import time
# importing binary tree structure
from binary_search_tree import BinarySearchTree

# starting time tracker
start_time = time.time()

# reading the names file
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# reading the names file
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# using hash sets to make even faster 0(1) and better than bst(logn)
names_set = set(names_2)

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# the first for loop checks each name in names_1, so the speed of that depends on n,
# the number of names in the list. the next for loop also checks for every name in names_2
# so depends on the number of names in the list, also n. So, we have n * n complexity, of n^2

# this solution ^^ is 0(n^2) for each entry in name_1 your also looping through each entry in name_2. # runtime: 6.446194887161255 seconds

# optimized solution  below os o(n)(logn) - looping once through each name/node(names_1 - 0(n)) in the bst (names_2 - logn)  runtime: 0.11794686317443848 seconds

# inserting names_1 list into bst (logn)
bst = BinarySearchTree(names_1[0])  # adding first name in tree
for i in range(1, len(names_1)):  # looping though remaining names and inserting into bst
    bst.insert(names_1[i])

# loop through each name in names_2 list and see if there's duplicates in the names_1 bst tree
for name in names_2:  # o(n)
    # check if bst contains duplicates by using contains method on bst class
    # if target name from names_2 is in tree then return true and append
    if bst.contains(name):
        duplicates.append(name)

# bst is optimized for searches, faster b/c each comparison allows the operations to skip about half of the tree, reduces potential answer by 2, or eliminate one side. avg case is logn, worst case to find an element is 0(n) b/c it could be a LL, and need to search thru the whole tree one at a time.

# using a hash set (hash table is the underlying data structure) is even fast than bst
# for name_1 in names_1:
#         if name_1 in names_set:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
