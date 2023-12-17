import io
try:
    file = open("data_1.txt",'w')
    file.write("hello world")
    data = file.read()
    print(data)
    
except io.UnsupportedOperation:
    print("cannot read/write file..")
finally:
    file.close()
    print("It will always executed..")