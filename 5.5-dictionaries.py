'''
dictionaries: unordered set of 'key: value' pairs
 A pair of braces creates an empty dictionary: {}.
 Performing list(d.keys()) on a dictionary returns
 a list of all the keys used in the dictionary,
 in arbitrary order (if you want it sorted,
 just use sorted(d.keys()) instead).
 To check whether a single key is in the dictionary, use the 'in' keyword.

'''
print('EXAMPLE ONE')
print('-'*11)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print()

del tel['sape']
tel['irv'] = 4127
print(tel)
print()

print( list(tel.keys()) )
print()

print( sorted(tel.keys()) )
print()

print( 'guido' in tel)
print()

print( 'jack' not in tel)
print()

print('-'*11)
print('EXAMPLE TWO')
print('-'*11)
#The dict() constructor builds dictionaries directly from sequences
#of key-value pairs:

print( dict([('ape', 123),('frog', 456),('toad', 789)]) )
print()

print('-'*11)
print('EXAMPLE THREE')
print('-'*11)
#In addition, dict comprehensions can be used to create dictionaries
#from arbitrary key and value expressions:

print( {x: x**2 for x in (2, 4, 6)} )
print()

print('-'*11)
print('EXAMPLE FOUR')
print('-'*11)
#When the keys are simple strings, it is sometimes easier to specify pairs
#using keyword arguments:

print( dict(deer=234, lion=456, tiger=876))




