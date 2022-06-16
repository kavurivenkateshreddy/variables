"""
Date: 19th April 2022 Tuesday
Name: kavuri venkatesh reddy
File Desc: variable rules,way to assign variables,isidentifier()
"""
'''alphabits > start : middle : end
   numerical >         middle : end
 under scrol > start : middle ; end
 we should not enter any space in between the variable 
 we can reuse the variables there is no limites for the naming of variables.
 
RULES OF VARIABLES:
-------------------------
1) A variable is mostly on left side.

2) Variables are used for storing the values.

3) Variables works like containers.

4) A variable should start with alphabet
   it can be lower case or upper case.

5) Python is case-sensitive.
   There is a d/b lower case and upper case letters.

6) Variables cannot contain keywords.

7) A Variable can't start with numeric.

8) A variable can start with underscore _ Symbol

9) Except underscore other symbols are not allowed.

10) A variable should not a space between them.
 '''
a=1;b=2
print(a) #1
print(b) #2
print(a);print(b) #1
                  #2
print(a,b) # 1 2
c,d,e=3,4,5
print(c) #
print(d) #4
print(e) #5
print(c,d,e) #3 4 5
print(c);print(d);print(e) #3
                           #4
                           #5
f=g=h=6;i=7;j=8
print(f) #6
print(g) #6
print(h) #6
print(f,g,h) #6 6 6
print(f,i,j) #6 7 8
# print(k) #Name Error: name 'k' is not defined
""" ISIDENTIFIER
---> isidentifier is used to find the variables are valied or invalied
---> is > it is in the form of bool(true or false)"""
print('a'.isidentifier()) #True
print('_'.isidentifier()) #True
print('_a'.isidentifier()) #True
print('a_'.isidentifier()) #True
print('1'.isidentifier())  #False
print('s_1'.isidentifier()) #True
print('n.1'.isidentifier()) #False
print('a 1_'.isidentifier()) #False
