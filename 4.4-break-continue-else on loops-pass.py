print("EXAMPLE ONE")
print("-----------")
print("-----------")


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n," equals ",x,"*",n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n,'is a prime number')

'''
the else clause belongs to the for loop, not the if statement

When used with a loop, the else clause has more in common
with the else clause of a try statement than it does that
of if statements: a try statement’s else clause runs when
no exception occurs,and a loop’s else clause
runs when no break occurs.
'''

print("-----------")
print("EXAMPLE TWO")
print("-----------")
print("-----------")

for num in range(2,10):
    if num % 2 == 0:
        print("found an even number ",num)
        continue
    print("found a number ",num)

'''
The continue statement, also borrowed from C,
continues with the next iteration of the loop
'''

print("-----------")
print("EXAMPLE 3")
print("-----------")
print("-----------")

'''
The pass statement does nothing. It can be used when a statement is
required syntactically but the program requires no action
'''
while True:
    pass #busy-wait for keyboard to intrrupt (Ctrl+C)

print("-----------")

# is commonly used for creating minial classes
class MyEmptyClass:
    pass


print("-----------")

# used as a place holder for a function or conditional body
def initlog(*args):
    pass #remember to implement this


