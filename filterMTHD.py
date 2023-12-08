def even(num):
    return num%2 == 0
def odd(num):
    return num%2 != 0
numbers = [42,65,321,14,41,98,78,77,55,33]
'''e = []
o = []
for i in range(len(numbers)):
    if even(numbers[i]):
        e.append(numbers[i])
    elif odd(numbers[i]):
        o.append(numbers[i])
print(e)
print(o)'''
print(list(filter(even,numbers)))
print(list(filter(odd,numbers)))

