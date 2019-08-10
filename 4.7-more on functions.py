print('example one')
print('-----------')

def ask_ok(prompt, retries=4, complaint='yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return False
        retries = retries-1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
#This example also introduces the 'in' keyword.
#This tests whether or not a sequence contains a certain value

#calling the function several ways
#1 giving only the mandatory argument
ask_ok('Do you really want to quit?')

#2 giving one of the optional arguments
ask_ok('OK to overwrite the file?',2)

#3 giving all arguments
ask_ok('OK to overwrite the file?',2,'come on only yes or no')


print()
print('example two')
print('-----------')

#default values are evaluated at the point of function definition

i = 5

def f(arg=i):
    print(arg)

i=6
f() #will print 5

print('-----------')
'''
Important warning: The default value is evaluated only once.
This makes a difference when the default is a mutable object
such as a list, dictionary, or instances of most classes.
For example, the following function accumulates the arguments
passed to it on subsequent calls:

'''

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print('-----------')
#If you don’t want the default to be shared between subsequent calls,
#you can write the function like this instead:

def f2(a, L=None):
    '''
    if L is None: 
        L = []
    '''
    L = [] #delete this line if u use the ones commented above
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))
