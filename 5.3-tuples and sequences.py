#a tuple consist of a number of values separated by commas
print('EXAMPLE ONE')
print('-'*11)

t = 12345, 54321, 'hello!'
print(t[0])
print(t)

#tuples may be nested
u = t, (1,2,3,4,5)
print(u)

#tuples are inmutable
#t[0] = 8888 #this line produces an error

#but they can contain mutable objects
v = ([1,2,3],[3,2,1])
print(v)


print()
print('EXAMPLE two')
print('-'*11)
'''
A special problem is the construction of tuples containing 0 or 1 items:
the syntax has some extra quirks to accommodate these.
Empty tuples are constructed by an empty pair of parentheses;
a tuple with one item is constructed by following a value with a comma
(it is not sufficient to enclose a single value in parentheses)
'''

empty = ()
singleton = 'hello', #<-- note trailing comma

print(len(empty))

print(len(singleton))

print(singleton)

print()
print('EXAMPLE 3')
print('-'*11)
'''
The statement t = 12345, 54321, 'hello!' is an example of tuple packing:
the values 12345, 54321 and 'hello!' are packed together in a tuple.
The reverse operation is also possible
'''
x, y, z = t
print(x)
print(y)
print(z)

'''
This is called, appropriately enough, sequence unpacking
and works for any sequence on the right-hand side.
Sequence unpacking requires that
there are as many variables on the left side of the equals sign
as there are elements in the sequence.
Note that multiple assignment is really just a combination
of tuple packing and sequence unpacking.
'''

