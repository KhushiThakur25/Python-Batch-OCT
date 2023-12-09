import random
positions = [i for i in range(9)]
occupied = []
def gameboard():
    print("""
            {} | {} | {}
            ------------
            {} | {} | {}
            ------------
            {} | {} | {}""".format(positions[0],positions[1],positions[2],
                                   positions[3],positions[4],positions[5],
                                   positions[6],positions[7],positions[8],))
def user_move(ch):
    pos = int(input("Enter the position.."))
    if pos in occupied:
        print("you can't move at this position..")
        user_move(ch)
    else:
        positions[pos] = ch
        occupied.append(pos)
    

def cpu_move(ch):
    pos = random.randint(0,8)
    if pos in occupied:
        cpu_move(ch)
    else:
        positions[pos] = ch
        occupied.append(pos)
    

def main():
    gameboard()
    user_ch = input("Enter your choice..X OR 0")
    if user_ch == "X":
        cpu_ch = "0"
    else:
        cpu_ch = "X"
    count = 0
    while count<5 :
        count += 1 
        user_move(user_ch)
        gameboard()
        cpu_move(cpu_ch)
        gameboard()
    
main()
