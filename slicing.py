'''
slicing: by using slicing ,we can access single character as well as group of character
from string,list and so on.

slicing also uses square brackets([])

the square brackets can contain two integers seperated by a colon(:)

the first integer is the start index , the second integers is the end index.
'''

text='Hello darshan'
print(text[2:8])

l=[6,8,9,0,6]
print(l[0:])

# note : in the slicing last integer value not count becoz indexing start from 0.

# To slice from a specific position until the end of the string,
# don't specify the second integer.

text='Hello Darshan'
print(text[0:])

list=[7,9,0,5,7]
print(list[0:])
