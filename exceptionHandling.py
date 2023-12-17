try:
    num_1 = int(input("Enter the first number.."))
    num_2 = int(input("Enter the second number.."))

    add = num_1 + num_2 
    sub = num_1 - num_2 
    div = num_1/num_2 
    mul = num_1*num_2 

except ValueError :
    print("Invalid input,Please enter a valid number..")
except ZeroDivisionError:
    print("Cannot divide by zero..")
except BaseException as msg:
    print(msg)
else:
    print("Sum is",add)
    print("Sub is",sub)
    print("Div is",div)
    print("Mul is",mul)
