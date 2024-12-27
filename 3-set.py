# Set are unordered collection of data types
# that are iterable , mutable and no duplicate elements
# built in function set()
# type of elements need not be same, can be various mixed-up values

set1= set()
print("An empty set")
print(set1)

set2= set("Geeksforgeeks")
print("\nset with use of string:", set2)
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

'''Access Set Items
Set items cannot be accessed by referring to an index, since sets are unordered the items have no index. But you 
can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in the keyword.'''

set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
    
print("\n ")
print("Geeks" in set1)