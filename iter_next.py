#an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#output
#b
#a
#n
#a
#n
#a
