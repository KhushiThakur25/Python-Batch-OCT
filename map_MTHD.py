def temp_convert(c):
    return 9/5*c + 32

def km_to_m(km):
    return km*1000
'''f = temp_convert(34.6)
print(f)'''
temp = [34.6,23.3,85.4,69.5,47.5,32.1,74.5]
kms = [122,321,54,64,879,10,546]

print(list(map(temp_convert,temp)))
print(list(map(km_to_m,kms)))

'''def my_map(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data'''



'''print(temp_convert(temp[0]))
print(temp_convert(temp[1]))
print(temp_convert(temp[2]))
print(temp_convert(temp[3]))'''

'''f = []
for t in temp:
    f.append(temp_convert(t))
    
print(f)
m = []
for km in kms:
    m.append(km_to_m(km))
    
print(m)'''
