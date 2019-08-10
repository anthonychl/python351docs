print('EXAMPLE ONE')
print('-------------')
#functions can be called by using keyword arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#the function can be called any of the following ways

parrot(1000)                                          # 1 positional argument
print('-------------')
parrot(voltage=1000)                                  # 1 keyword argument
print('-------------')
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
print('-------------')
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
print('-------------')
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
print('-------------')
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
print('-------------')

#but all the following calls would be invalid:

#parrot()                     # required argument missing
print('-------------')
#parrot(voltage=5.0,'dead')   # non-keyword argument after a keyword argument, u have 2 specify the kw
print('-------------')
#parrot(110, voltage=220)     # duplicate value for the same argument
print('-------------')
#parrot(actor='John Cleese')  # unknown keyword argument
print('-------------')

print()
print('EXAMPLE two')
print('-------------')

'''
when an argument of the form **name is present the function recieves
a dictionary.... when the argument is of the form *name it recieves
a tuple

when we declare a function *name must occur befor **name
'''

def cheeseshop(kind,*arguments,**keywords):
    print('do you have any ',kind,' sir?')
    print("i'm sorry we r all out of ",kind,' sir')
    for arg in arguments: #prints the whole tuple
        print(arg)  
    print("-"*40)
    keys = sorted(keywords.keys()) #sorts & stores the keywords alphabetically(only the keys not their values, so is not a new dictionary is a list)
    for kw in keys: #prints the dictionary keywords sorted
        print(kw, ":", keywords[kw])

cheeseshop('limburger', "it's very funny sir","it's really very funny",shopkeeper='michael',client='john',sketch='cheese shop sketch')
    
print()
print('EXAMPLE 3')
print('-------------')

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

textfile=open("items.txt",'w')
textfile.close()

textfile=open("items.txt",'a')
write_multiple_items(textfile,'/','one','two','sdf')
textfile.close()


print()
print('EXAMPLE 4')
print('-------------')

def concat(*args, sep='/'):
    return sep.join(args)

print( concat('earth','venus','mars') )

print( concat('earth','venus','mars',sep='.') )

print()
print('EXAMPLE 5')
print('-------------')

print( list( range(3,6) ) ) #normal call with separate arguments

args = [3,6]
print( list( range(*args) )) #call with arguments unpacked from a list


print()
print('EXAMPLE 6')
print('-------------')
#unpacking args from dictionary

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

d = {"voltage":"four million","state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
