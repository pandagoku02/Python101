'''5. Dictionary Data Type in Python
A dictionary in Python is an unordered collection of data values, used to store data values like a map, 
unlike other Python Data Types that hold only a single value as an element, a Dictionary holds a key: value pair. 
Key-value is provided in the dictionary to make it more optimized. 
Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.'''

Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)


#Accessing Key-value in Dictionary
#In order to access the items of a dictionary refer to its key name. Key can be used inside square brackets. 
#There is also a method called get() that will also help in accessing the element from a dictionary.

Dict = {1:'First', 2:'Double', 3:'Cosmos', 8: 234}

print("Dictionary elements mixed values:\n",Dict)
print(Dict[1])
print("Access element using get:", Dict.get(3))