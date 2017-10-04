hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print('You should enter numeric value, please try again')
    quit(12)

irate = input("Enter Rate:")
rate = float(irate)
if h > 40.0:
    pay = (40 + 1.5 * (h - 40)) * rate
else:
    pay = h * rate

print(pay)
