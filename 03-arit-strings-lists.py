Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 12/3
4.0
>>> 12/8
1.5
>>> 12/8
1.5
>>> 12//8
1
>>> 12%5
2
>>> 5**2
25
>>> 2**7
128
>>> width=20
>>> height=5*9
>>> width*height
900
>>> n
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> 3* 3.75/1.5
7.5
>>> 7.0/2
3.5
>>> 7/2
3.5
>>> tax = 12.5/100
>>> price=100.50
>>> price*tax
12.5625
>>> price+_
113.0625
>>> round(_,2)
113.06
>>> 3+5j * 4j
(-17+0j)
>>> #---------------------
>>> 'spam'
'spam'
>>> "spam"
'spam'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
>>> '"yes", he said
SyntaxError: EOL while scanning string literal
>>> '"yes",he said'
'"yes",he said'
>>> s='first line\n second line'
>>> s
'first line\n second line'
>>> print(s)
first line
 second line
>>> print('c:\some\name')
c:\some
ame
>>> print(r'c:\some\name') # add the r to use raw strings
c:\some\name
>>> #it skipped the \n character
>>> #---------
>>> print("""\
Usage: thingy [OPTIONS]
	-h         display this usage msg
	-H         hostname to connect to
""")
Usage: thingy [OPTIONS]
	-h         display this usage msg
	-H         hostname to connect to

>>> #--------------
>>> # three times 'un' followed by 'ium'
>>> 3*'un'+'ium'
'unununium'
>>> 'Py' 'thon'
'Python'
>>> prefix = 'py'
>>> prefix 'thon' # cant concateate variable and a strin literal
SyntaxError: invalid syntax
>>> prefix + 'thon' # using the + now you can
'python'
>>> text = ('put several strings' 'within parenthesis' 'to have them joined together')
>>> text
'put several stringswithin parenthesisto have them joined together'
>>> word = 'python'
>>> word[0]
'p'
>>> word[5]
'n'
>>> word[-1] #last char
'n'
>>> word[-2] # second-last char
'o'
>>> word[:2]
'py'
>>> word[2:]
'thon'
>>> word[:2] #chars from position 0(included)to 2(excluded)
'py'
>>> word[2:5] #chars from position 2(included)to 5(excluded)
'tho'
>>> word[:2]+word[2:]
'python'
>>> word[42]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    word[42]
IndexError: string index out of range
>>> word[2:42] #with slicing there's no error msg
'thon'
>>> #-----------
>>> #cannot reassign value to a position
>>> word[0]=j
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    word[0]=j
NameError: name 'j' is not defined
>>> word[2:]='py'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    word[2:]='py'
TypeError: 'str' object does not support item assignment
>>> s='asdfhqwihvnsdjfksdl'
>>> len(s)
19
>>> #len() returns length of string
>>> #------------------------
>>> #----- lists ------------
>>> #------------------------
>>> 
>>> squares=[1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> #lists can be also indexed and sliced
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> #concatenation
>>> squares + [45,78,56,75,100]
[1, 4, 9, 16, 25, 45, 78, 56, 75, 100]
>>> #unlike strings wich are inmutable, lists ARE mutable
>>> cubes=[1,8,27,65,125]
>>> cubes[3]=64
>>> cubes
[1, 8, 27, 64, 125]
>>> #add items using apped
>>> cubes.append(216)
>>> cubes.append(7**3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> #assignment to slices is also possible
>>> letters = ['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5]=['C','D','E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5]=[]
>>> letters
SyntaxError: multiple statements found while compiling a single statement
>>> letters[2:5]=[]
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:]=[]
>>> letters
[]
>>> letters=['a','b','c']
>>> len(letters)
3
>>> #its possible to nest lists(build lists containing other lists)
>>> n=[1,2,3]
>>> x=[letters,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[1]
[1, 2, 3]
>>> x[0][1]
'b'
>>> x[1][2]
3
>>> #--------------------------
>>> #-- prog example------------
>>> #-- fibonacci series------
>>> 
>>> a,b=0,1
>>> while(b<10)
SyntaxError: invalid syntax
>>> while b<10:
	print(b)
	a,b=b,a+b

	
1
1
2
3
5
8
>>> a,b = 0,1
>>> while b<1000:
	print(b,end=',')
	a,b=b,a+b

	
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> 
