Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (1,2,3,4,5,6,8,9,45)
>>> type(tup)
<class 'tuple'>
>>> tups = 2,6,5,8
>>> type(tups)
<class 'tuple'>
>>> tup = 5
>>> type(tup)
<class 'int'>
>>> a = 5
>>> b = 6
>>> a+b
11
>>> tup = 5,
>>> type(tup)
<class 'tuple'>
>>> tup = (1,2,3,4,5,6,8,9,45)
>>> len(tup)
9
>>> tup.count(3)
1
>>> tup = (1,2,3,4,5,3,8,3,45)
>>> tup.count(3)
3
>>> tup.index(3)
2
temp = list(tup)
type(temp)
<class 'list'>
temp
[1, 2, 3, 4, 5, 3, 8, 3, 45]
temp.append(100)
temp
[1, 2, 3, 4, 5, 3, 8, 3, 45, 100]
temp.pop(3)
4
temp
[1, 2, 3, 5, 3, 8, 3, 45, 100]
temp[3] = 89
temp
[1, 2, 3, 89, 3, 8, 3, 45, 100]
tup = tuple(temp)
type(tup)
<class 'tuple'>
tup
(1, 2, 3, 89, 3, 8, 3, 45, 100)
states = up , mp, rajasthan , gujarat , himachal pradesh, delhi  [add- 3,5 , delete-4,2]
SyntaxError: invalid syntax
states = "up" , "mp", "rajasthan" , "gujarat" , "himachal pradesh", "delhi"
type(states)
<class 'tuple'>
temp = list(states)
type(temp)
<class 'list'>
temp[3] = "goa"
temp
['up', 'mp', 'rajasthan', 'goa', 'himachal pradesh', 'delhi']
temp[5] = "chennai"
temp
['up', 'mp', 'rajasthan', 'goa', 'himachal pradesh', 'chennai']
states = "up" , "mp", "rajasthan" , "gujarat" , "himachal pradesh", "delhi"
temp = list(states)
temp.insert("goa")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    temp.insert("goa")
TypeError: insert expected 2 arguments, got 1
temp.insert("goa",3)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    temp.insert("goa",3)
TypeError: 'str' object cannot be interpreted as an integer
temp.insert(5,3)
temp
['up', 'mp', 'rajasthan', 'gujarat', 'himachal pradesh', 3, 'delhi']
temp[3] = "goa"
temp[5] = "chennai"
temp
['up', 'mp', 'rajasthan', 'goa', 'himachal pradesh', 'chennai', 'delhi']
temp.pop(4)
'himachal pradesh'
temp.pop(2)
'rajasthan'
temp
['up', 'mp', 'goa', 'chennai', 'delhi']
states = tuple(temp)
type(states)
<class 'tuple'>
states
('up', 'mp', 'goa', 'chennai', 'delhi')
s = {2,4,2,6}
type(s)
<class 'set'>
s
{2, 4, 6}
s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s
set()
KeyboardInterrupt
s = {2,4,2,6}
for value in s:
    print(value)

2
4
6
