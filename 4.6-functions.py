print("example one")
print('-----------')

def fib(n): # write Fobonacci series up tp n
    """print a fibonacci series up to n"""
    a,b = 0,1
    while a<n:
        print (a, end=' ')
        a,b = b,a+b
    print()

fib(2000)    

print()

f=fib #renaming mechanism

f(100)

print()

fib(0) #prints nothing 'cause the interpreter supresses None

print()

print(fib(0)) #now we can see a built-in value called None

print()
print("example two")
print('-----------')

def fib2(n): #return fibonacci series up to n
    """Return a list containing the fibonacci series up to n"""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result
'''
f100 = fib2(100) # call it
print(f100) #write the result
'''
print(fib2(100))
