# string slicing to rotate a string
string = "Brainmentors"
k = 2
#left rotate = "ainmentors-Br"
#right rotate = "rs-Brainmento"

left1 = string[:2]
left2 = string[2:]
right1 = string[:len(string)-2]
right2 = string[len(string)-2:]
str_left = left2 + left1
str_right = right2 + right1
print("left rotation is:",str_left)
print("right rotation is:",str_right)
