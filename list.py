#list.append(x)
#list.extend(iterable)
#list.insert(i, x)
#list.remove(x)
#list.pop([i])
#list.clear()
#list.index(x[,start[,end]])
#list.count(x)
#list.sort(*, key=None, reverse=False)
#list.reverse()
#list.copy()

lst1 = [[1,2,3],[3,2,1]]
lst2 = lst1

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
fruits.append('melon')
print(fruits)
print(fruits.index('banana'))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)

squares = [x**2 for x in range(10)]
print(squares)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rearrangeMatrix = [[row[i] for row in matrix] for i in range(4)]
print(rearrangeMatrix)

rearrangeMatrix = [[row[i] for row in matrix[0:2]] for i in range(3)]
print(rearrangeMatrix)

rearrangeMatrix = matrix
print(rearrangeMatrix)

rearrangeMatrix = list(zip(*matrix))
print(rearrangeMatrix)

rearrangeMatrix = [sum(row) for row in matrix]
print(rearrangeMatrix)

lst1 = [2,3,5,1,3]
print(max(lst1))

