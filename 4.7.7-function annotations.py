'''
Function annotations are completely optional metadata information
about the types used by user-defined functions

Annotations are stored in the __annotations__ attribute of the function
as a dictionary and have no effect on any other part of the function.
Parameter annotations are defined by a colon after the parameter name,
followed by an expression evaluating to the value of the annotation.
Return annotations are defined by a literal ->,
followed by an expression, between the parameter list
and the colon denoting the end of the def statement
'''

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


print(f('spam'))
print('------------')
print(f('smoked ham','scrambled eggs'))
print('------------')
print(f()) #error, must give a value to ham
print('------------')
