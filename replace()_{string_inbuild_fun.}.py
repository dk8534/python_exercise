'''
Replce() : replace function only works with strings.
           Replace function replace the specified substring with another substring
           It does not modify old string and give new modify string .
Syntax: string.replace(old substring,new sub string,count)
*old substring: mendatry to define,type of old substring should be same 
*new substring: mendatry to define
*count: not mendatry to define or used for no. replce of substring

'''

text="he is boy,his name is darshan"
val1=text.replace("is","was") # produce an error in string because in "his" is 
                              # also replace with was so remove this error from new string  
                              # give space before and after from is like " is "
val2=text.replace(" is "," was ")
val3=text.replace(" is "," was ",1) # using count value replce value first time 
                                    # that are use in after he  
print(val1)
print(val2)
print(val3)
 
#=========================================================================================

text="HE IS BOY,HIS NAME IS DARSHAN"
x=text.replace(" is "," WAS ") # old substring type should be same
                               # lower with lower or upper with upper 
print(x)

Y=text.replace(" IS "," WAS ")
print(Y)