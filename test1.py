print(5==5)
print(5==6)
x = 2
y = 21
if x%2 == 0:
    print('x is even')
else:
    print('x is odd')
if x < 20:
    print('x is small')
else:
    print('x is lager')
if x < y:
    print('x is less than y')
elif x > y:
    print('x is grater than y')
else:
    print ('x and y are equal')
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is grater than y')
if 0 < x:
    if x < 10:
        print('x is a possitve single digit number')
if 0 < x and x < 10:
     print('x is a possitve single digit number')
     
prompt = "What is the air velocity of an unladen swallow?\n"
speed = input(prompt)
int (speed)

inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
