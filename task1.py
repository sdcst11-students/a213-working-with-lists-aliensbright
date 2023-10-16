#!python3

"""
Create a LIST that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""


print('Today we will find what type of animal you are!\n\n')
animals = ['Cat','Fish','Dog','Bear','Turtle']
animals.sort()
x=int(input('Enter your favourite number to determine what animal you are.==>'))
x=x%5
print(animals[x])