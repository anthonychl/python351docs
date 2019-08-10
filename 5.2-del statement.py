'''
There is a way to remove an item from a list given its index
instead of its value: the del statement.
This differs from the pop() method which returns a value.
The del statement can also be used to remove slices from a list
or clear the entire list (which we did earlier
by assignment of an empty list to the slice).
For example
'''

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] #deletes the value in index 0
print(a)

del a[2:4] #deletes the values of index 2 and 3
print(a)

del a[:] #deletes values of all indexes, deletes all
print(a)

#'del' can also be used to delete entire variables
del a
#referencing the name 'a' after this is an error
#until another value is assingned to 'a
print(a)

