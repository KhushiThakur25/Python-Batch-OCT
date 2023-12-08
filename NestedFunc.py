#nested function
def calc():
    x = 6
    y = 7
    #print("i'm calc")
    def add():
        z1 = x+y
        return z1
    def sub():
        z2 = x-y
        return z2
    #print(add(),sub())
    return add,sub
add,sub = calc()
print(add())
print(sub())
