'''
indexing : by using of indexing , we can access a single chacter .

indexing uses square brackets ([]) to access chacters .

always indexing start from 0 where 0 represents to first character,
and 1 represents the second character and so on.

during the indexing it's count every type of character , numbers, 
special character,and so on.
'''


#indexing in string
text = 'Hello darshan'
print(text[0])
print(text[1])
print(text[9])

#indexing in number / list
list=[4,5,6,7,8,9] 
print(list[0])
print(list[1])
print(list[9]) # give an error:list index out of range
               # becoz in the above list no. of integers is 


# negative indexing: 
'''negative indexing not start from 0 always start from -1 
   where -1 represent the last charcter / number 
   -2 represent second to the last charcter / number
'''
text= 'Hello darshan'
print(text[-1])
print(text[-2])


