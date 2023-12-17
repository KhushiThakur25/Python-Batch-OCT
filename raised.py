def atm():
    total = 10000
    pin = input("Enter the pin..")
    if pin == "1234":
        print("Login success..")
    else:
        raise ValueError("Login failed..")
    
    amount = int(input("Enter the amount.."))
    if amount > total:
        raise ValueError("Insufficient Balance")
    else:
        total -= amount
        print("Remaining balance is",total)
try:
    atm()
except ValueError as msg:
    print(msg)