list1 = [1,2,3,'ayan']
print(list1)

#append(), extend() and insert

list1.append(('biswas',0))
print(list1)
list1.extend((3,4))
print(list1)

list1.insert(2,'hi')
print(list1)

#del is a keyword not a function ,pop(),remove()

del list1[3]
print(list1)

a = list1.pop(4) #it returns the number deleted
print(a)

list1.remove('hi')
print(list1)

print(list1)
print(list1[0:3]) #fisrt 3 elements
print(list1[0:4:2]) #first four elements in gap of 2
print(list1[::-1]) #print list in reverse order



