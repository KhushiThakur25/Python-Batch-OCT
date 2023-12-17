def func():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index.."))
        print(l[i])
        return 1
    except:
        print("something went wrong..")
        return 0

    finally:
        print("always executed...")

x = func()
print(x)