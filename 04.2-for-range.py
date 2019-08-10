print('EXAMPLE ONE')
print('===========')
#measure some strings
words = ['cat','window','defenestrate']

for w in words:
    print(w,len(w))


#----------------------------------
print(' ')
print('===========')
print('EXAMPLE TWO')
print('===========')

words2 = ['cat','window','defenestrate']

for w2 in words2[:]:  #loop over a slice copy of the entire list
    if len(w2) > 6:
        words2.insert(0,w2)

print(words2)

#----------range() function------------------------
print(' ')
print('===========')
print('EXAMPLE THREE')
print('===========')

print('for i in range(5)')
for i in range(5):
    print(i)

print('for i in range(5,10)') #range(start,stop)
for i in range(5,10):
    print(i)

print('for i in range(0,10,3)') #range(start, stop, step)
for i in range(0,10,3):
    print(i)

print('for i in range(-10,-100,-30)') #same but negative numbers
for i in range(-10,-100,-30):
    print(i)

print(' ')
print('===========')
print('EXAMPLE FOUR')
print('===========')

print("a = ['mary','had','a','little','lamb']\nfor i in range(len(a)):\nprint(i, a[i])  ")
      
a = ['mary','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])    
    
print(' ')
print('===========')
print('EXAMPLE FIVE')
print('===========')

'''
range() behaves like a list but is an iterable object

the 'for' statement is an iterator and the function 'list()' is another
'''

print("print(range(10))")
print(range(10))

print("")
print("print(list(range(5)))")
print(list(range(5)))







