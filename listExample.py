mylist = [1,2,3]
print len(mylist)

print mylist

print mylist * 4
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print 1 in mylist

print 4 in mylist

print mylist[:1]

biglist = [['Dilbert', 'Dogbert', 'Catbert'], ['Wally', 'Alice', 'Asok']]

print biglist[0][2]
biglist[1] = 'Ratbert'
print biglist[1]

stacklist = biglist[0]
stacklist = stacklist + ['The boss']
print stacklist

stacklist.pop()
print stacklist
stacklist.pop()
print stacklist
stacklist.extend(['Alice', 'Carol', 'Tina'])
print stacklist
stacklist.reverse()
print stacklist
del stacklist[1]
print stacklist
