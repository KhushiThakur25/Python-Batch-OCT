Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
string = "Brainmentors"
print(string[-3])
o
print(string[:-3])
Brainment
print(string[:len(string)-2])
Brainmento
k = 2
print(string[:len(string)-k])
Brainmento
k = 3
print(string[:len(string)-k])
Brainment

========================== RESTART: C:/Python312/RotateString.py =========================
left rotation is: ainmentorsBr
right rotation is: rsBrainmento

========================== RESTART: C:/Python312/UppercaseQS.py ==========================
this is a pyTHON LANGUAGE

========================== RESTART: C:/Python312/UppercaseQS.py ==========================
THIS IS A PY
hon language

========================== RESTART: C:/Python312/UppercaseQS.py ==========================
THIS IS A PYT
hon language
lists = [2,3,4,5,6]
print(lists)
[2, 3, 4, 5, 6]
lists[2]
4
lists[-2]
5
lists[:3]
[2, 3, 4]
lists[::-1]
[6, 5, 4, 3, 2]
if 4 in lists:
    print("yes")
else:
    print("No")

yes
if 8 in lists:
    print("yes")
else:
    print("No")

No
lists = [i for i in range(10)]
lists
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lists = [i*i for i in range(10)]
lists
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
for i in lists:
    if i%2 == 0:
        print(i)

0
4
16
36
64
lists.appened(100)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    lists.appened(100)
AttributeError: 'list' object has no attribute 'appened'. Did you mean: 'append'?
lists.append(100)
lists
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lists.append(121)
lists
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
lists = [45,2,36,78,94,56]
lists.sort()
lists
[2, 36, 45, 56, 78, 94]
lists.sort(reversed = True)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    lists.sort(reversed = True)
TypeError: 'reversed' is an invalid keyword argument for sort()
lists.sort(reverse = True)
lists
[94, 78, 56, 45, 36, 2]
lists.reverse()
lists
[2, 36, 45, 56, 78, 94]
lists.index(45)
2
lists = [45,2,36,78,94,56,2,2,2]
lists.count(2)
4
lists2 = lists
lists2[0] = 100
print(lists2)
[100, 2, 36, 78, 94, 56, 2, 2, 2]
print(lists)
[100, 2, 36, 78, 94, 56, 2, 2, 2]
lists3 = lists.copy()
lists3[0] = 200
lists3
[200, 2, 36, 78, 94, 56, 2, 2, 2]
lists
[100, 2, 36, 78, 94, 56, 2, 2, 2]
lists.insert(2,456)
lists
[100, 2, 456, 36, 78, 94, 56, 2, 2, 2]
[100, 2, 456, 36, 78, 94, 56, 2, 2, 2]
[100, 2, 456, 36, 78, 94, 56, 2, 2, 2]
lists.insert(3,[23,45,65])
>>> lists
[100, 2, 456, [23, 45, 65], 36, 78, 94, 56, 2, 2, 2]
>>> lists[3][1]
45
>>> lists.extend([23,45,65])
>>> lists
[100, 2, 456, [23, 45, 65], 36, 78, 94, 56, 2, 2, 2, 23, 45, 65]
>>> lists = [1,2,3,4,5,6]
>>> lists2 = [7,8,9]
>>> list1 = lists + lists2
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lists.extend(3,[23,45,65])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    lists.extend(3,[23,45,65])
TypeError: list.extend() takes exactly one argument (2 given)
>>> a = 3
>>> b = 5
>>> print(a,b)
3 5
>>> a,b = b,a
>>> print(a,b)
5 3
>>> a,b,c = 4,2,6
>>> print(a,b,c)
4 2 6
