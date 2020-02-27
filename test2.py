hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
Pay = hours * rate
print("Pay:",Pay)
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)

limit_hours = 40.0;

if h <= limit_hours :
    pay = (h)*(r)
else :
    pay = (limit_hours)*(r) + (h - limit_hours)*(r*1.5)

print(str(pay))
