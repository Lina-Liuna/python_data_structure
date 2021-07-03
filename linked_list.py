import llist
from llist import sllist, sllistnode

mylist = sllist([1,2,3,4,5])
print(mylist)
print(mylist.first)
print(mylist.last)
print(mylist.size)
mylist.append(6)
print(mylist)
node = mylist.nodeat(5)
mylist.insertafter(7, node)
node = mylist.nodeat(0)
mylist.insertbefore(0,node)
print(mylist)
print(node.next)
print(node.next.value)
mylist.pop()
print(mylist)