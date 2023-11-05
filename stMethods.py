Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "khushi"
st[0]
'k'
st[0]="h"
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    st[0]="h"
TypeError: 'str' object does not support item assignment
del st[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    del st[0]
TypeError: 'str' object doesn't support item deletion
x = 'ram'
type(x)
<class 'str'>
x= "ram"
type(x)
<class 'str'>
print(x)
ram
x= ""ram""
SyntaxError: invalid syntax
x= '"ram"'
print(x)
"ram"
x= "'ram'"
print(x)
'ram'
text = "C:\Users\ASUS\Desktop"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
text = "Hello \n world"
text
'Hello \n world'
print(text)
Hello 
 world
text = "C:/Users/ASUS/Desktop"
print(text)
C:/Users/ASUS/Desktop
text = "C:/Users/ASUS/Desktop"

text = "C:\\Users\\ASUS\\Desktop"
text = r"C:\Users\ASUS\Desktop"
text = "Hello world"
text[5]
' '
text[7]
'o'
text[-3]
'r'
text[2:6]
'llo '
text[2:7]
'llo w'
text[5:]
' world'
text[:9]
'Hello wor'
text[:]
'Hello world'
text[-11:0]
''
text[len(text)-1:-11]
''
text[len(text)-1:0:-1]
'dlrow olle'
text[len(text)-1:-1:-1]
''
text[len(text)-1:1:-1]
'dlrow oll'
text[len(text)-1::-1]
'dlrow olleH'
text[::]
'Hello world'
text[::-1]
'dlrow olleH'
text[::2]
'Hlowrd'
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
st = "This is the python course"

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
"hello" == "Hello"
False
"hello".casefold() == "Hello".casefold()
True
"hellO".casefold() == "HeLlo".casefold()
True

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
2

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
3

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
2

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
2
2

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
2
2
5

============================ RESTART: C:/Python312/strClass.py ===========================
this is the python course
THIS IS THE PYTHON COURSE
This is the python course
This Is The Python Course
THIS IS ThE pYTHON COuRSE
2
2
5
2
>>> st = "this is tHe Python coUrse"
>>> st.index("z")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    st.index("z")
ValueError: substring not found
>>> st.find("z")
-1
>>> print(st[len(st)-1:1:-1])
esrUoc nohtyP eHt si si
>>> print(st[len(st)-1:0:-1])
esrUoc nohtyP eHt si sih
>>> print(st[len(st)-1:-1:-1])

>>> print(st[len(st)-1:-1:-1])

>>> n = -1
>>> print(st[len(st)-1:n:-1])

