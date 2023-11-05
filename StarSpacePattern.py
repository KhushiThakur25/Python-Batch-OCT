row = 5
for i in range(row):
    for j in range(row-i-1):
        print(" ",end = " ")
    for k in range(row-i-1,row):
        print("*",end=" ")
    print()    
