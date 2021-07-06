#Generators ---------yield
#   .Generators are a simple and powerful tool for creating iterators.
#   .Generators are written like regular functions but use the yield statement whenever they want to return data

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        if data[index] != 0:
            yield data[index]

for char in reverse([0, 1, 2, 0, 4, 0, 5]):
    print(char)

print(next(iter(reverse('rocket'))))