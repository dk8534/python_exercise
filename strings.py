'''
SYNTAX : '.......strings/text......'  -> (an valid string)
         ".......strings/text......"  -> (also valid string)
        
#single and double quotes together in single string

rules: 
1} together same category quotes can not be use in single text
or,
2} in single string quotes should be different

e.g:
    'dk said that"priyanshu is his younger brother" '  -> valid string
    "dk said that'priyanshu is his younger brother' "  -> valid string
    'dk said that"priyanshu is his younger brother' '  -> invalid string
    "dk said that"priyanshu is his younger brother" "  -> invalid string
'''

text= 'dk said that"priyanshu is his younger brother" '
print(text)

text= "dk said that'priyanshu is his younger brother' "
print(text)

'''
How to use same category quotes in single string:

rule: to use same category quotes in single string 
      , put backslash(\) before quotes character.
'''

text= 'let\'s go to school'
print(text)

text= "dk said that\"priyanshu is his younger brother\" "
print(text)



