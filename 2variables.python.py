#variables need not be declared in python

a=3
A=4
print(a)
print(A)
#Data type
""" Integers Floats Straings Lists Tuples Dictionaries"""
# Indentation to define blocks of code
# four spaces for indentation

#Operators
"""Arithmetic operators: +, -, *, /, %, ** (exponentiation), // (floor division).
Comparison operators: ==, !=, <, >, <=, >=.
Logical operators: and, or, not.
Assignment operators: =, +=, -=, *=, /=, %=, **=, //=.
Bitwise operators: &, |, ^, ~, <<, >>."""

# Print Output

print("Hello")
# print single and multiple variable

name = "Alice"
age = 30
print("Name:",name,'\n','Age:',age)

# Format Output Handling
# format() method, manipulation sep and end parameters
# f-string and % operator

amount = 150.75
print("Amount: ${:.2f}".format(amount))

# using sep and end 
# end parameter with '@'
print("Python",end='@')
print("GeeksforGeeks")

# separating with comma
print('G','F','G',sep=',')

# using f-string

name= 'Tushar'
age=23
print(f"Hello my name is {name} and I'm {age} years old")

#using % operator
"""%d –integer
%f – float
%s – string
%x –hexadecimal
%o – octal"""

# taking input from user

num = int(input("Enter a value:"))

add = num +5
print ("The sum is %d" %add)


# take multiple input using split method

x,y = input("enter two values: ").split()
print("Number of boys:",x)
print("Number of girls:",y)

# by default input is accepted as string , typecaast it to int 

n = input("how many roses?:")
print(n)

u