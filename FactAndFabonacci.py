#  factorial program
num = -2
product = 1
if num < 0:
    print("number is negative..")
elif num == 0:
    print("factorial is 1..")
else:
    while num>1:
        product *= num
        num -= 1
    print(product)
    
#   fabonacci program

num_1,num_2 = 0,1
for i in range(10):
    print(num_1,end = " ")
    result = num_1 + num_2
    num_1 = num_2
    num_2 = result
