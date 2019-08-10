print('EXAMPLE ONE')
print('------walking u through it-----')
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

print()
print('EXAMPLE TWO')
print('------walking u through it-----')

squares = list(map(lambda x: x**2, range(10)))
print(squares)

print()
print('EXAMPLE 3')
print('-------this is it----')

squares = [x**2 for x in range(10)]
print(squares)

'''
A list comprehension consists of brackets containing an expression
followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression
in the context of the for and if clauses which follow it.

For example, this listcomp combines the elements of two lists
if they are not equal:

'''
print()
print('EXAMPLE 4')
print('-------this is another----')

listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(listcomp)

print('-------and its equivalent----')
#Note how the order of the for and if statements is the same in both
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print(combs)

print()
print('EXAMPLE 5')
print('----------------')

vec = [-4, -2, 0, 2, 4]
#create a new list w/ the values doubled
vec = [x*2 for x in vec]
print(vec)

#filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

#apply a function to all the elements
print([abs(x) for x in vec])

#call a method on each element
freshfruit = ['   banana     ', '  loganberry    ', '   passion fruit ']
print(freshfruit)
freshfruit = [var.strip() for var in freshfruit]
print(freshfruit)

#create a list of two tuples like (number,square)
#the tuple must be parenthesized otherwise an error is raised
l = [(x,x**2) for x in range(6)]
print(l)

#fatten a list using a listcomp w/ two 'for'
vec = [(1,2,3),(4,5,6),(7,8,9)]
print( [num for elem in vec for num in elem] )


print()
print('EXAMPLE 6')
print('----------------')
#List comprehensions can contain complex expressions and nested functions:
from math import pi
print( [str(round(pi,i)) for i in range(1, 6)] )



















