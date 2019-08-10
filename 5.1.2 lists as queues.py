#lists as queues FIRST IN - FIRST OUT

'''
lists are not efficient for this purpose.
While appends and pops from the end of list are fast,
doing inserts or pops from the beginning of a list is slow
(because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque
which was designed to have fast appends and pops from both ends. 

'''

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)

print(queue.popleft())  #FIFO

print(queue.popleft())

print(queue)

