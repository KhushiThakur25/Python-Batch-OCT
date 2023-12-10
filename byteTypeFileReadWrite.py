file = open('mysticker.png','rb')
data = file.read()
print(data)
file.close()

#write operation on byte file

file = open('mysticker_2.png','wb')
file.write(data)
file.close()