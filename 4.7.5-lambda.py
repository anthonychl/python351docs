print('EXAMPLE ONE' )
print('---------')

def make_incrementor(n):
    return lambda x:x + n

f = make_incrementor(42)

print( f(0) )
print('---------')
print( f(1) )

print()
print('EXAMPLE TWO' )
print('---------')

pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]

pairs.sort(key=lambda pair:pair[1]) 
'''
pairexample = [(pos0,pos1),(pos0,pos1)]
pairexample.sort(key=lambda pair:pair[1]) 
sorts alphabetically by marking position 1
'''
print(pairs)

print()
print('---------')

pairs2 = [(2,'two'),(1,'one'),(4,'four'),(3,'three')]
pairs2.sort(key=lambda pair:pair[0])  #sorts by number by marking position 0
print(pairs2)

pairs2.sort(key=lambda pair:pair[1])  #sorts alphabetically by marking position 1
print(pairs2)
