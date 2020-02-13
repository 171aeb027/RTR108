Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 ==5
True
>>> 5 ==6
False
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> 
>>> x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')
SyntaxError: multiple statements found while compiling a single statement
>>> type (true)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type (true)
NameError: name 'true' is not defined
>>> type(5==5)
<class 'bool'>
>>> type(5==6)
<class 'bool'>
>>> x ! = y
SyntaxError: invalid syntax
>>> 17 and tru
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    17 and tru
NameError: name 'tru' is not defined
>>> x > 0 and x < 10
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x > 0 and x < 10
NameError: name 'x' is not defined
>>> if x > 0:
	print(5)

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    if x > 0:
NameError: name 'x' is not defined
>>> x = 5
>>> x
5
>>> print(5)
5
>>> if x < 0
SyntaxError: invalid syntax
>>> if x < 0:
	pass

>>> x = 3
>>> if x < 10
SyntaxError: invalid syntax
>>> if x < 10:
	print(8)

	
8
>>> x = 3
>>> if x < 10:
	print(6)
	print(9)
  File "<stdin>",line 3
  
SyntaxError: unindent does not match any outer indentation level
>>> print(9)
9
>>> print(11)
11
>>> x = 5
if x == 5 : 
    print('Equals 5')
if x > 4 : 
   print('Greater than 4')
if  x >= 5 :
    print('Greater than or Equals 5')
if x < 6 : print('Less than 6') 
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')
    
SyntaxError: multiple statements found while compiling a single statement
>>> x = 5
if x == 5 : 
    print(5)

    
if x > 4 : 
   print(6)
if  x >= 5 :
    print(5)
if x < 6 : print('Less than 6') 
if x <= 5 :
    print(4)
if x != 6 :
    print('8)
	  
SyntaxError: multiple statements found while compiling a single statement
>>> x = 5
	  
>>> if x == 5:
	  print (5)

	  
5
>>> if x > 4:
	  print(7)

	  
7
>>> if x > = 5:
	  
SyntaxError: invalid syntax
>>> print(7)
	  
7
>>> 
	  
>>> if x <= 6
	  
SyntaxError: invalid syntax
>>> if x <= 6:
	  print(9)

	  
9
>>>  x = 5
 if x > 2 :
     print(5)
     print(3)
 print(2)
	  
SyntaxError: unexpected indent
>>> if x%2 == 0:
	  print(4)

	  
>>> if x%2 == 0 :
	  print(4)

	  
>>> else:
	  
SyntaxError: invalid syntax
>>> if x%2 == 0:
	  print(4)
	  else :
	  
SyntaxError: invalid syntax
>>> 
