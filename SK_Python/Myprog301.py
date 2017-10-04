hrs = input("Enter Hours:")
h = float(hrs)
irate = input("Enter Rate:")
rate = float(irate)
if h > 40.0:
    pay = (40 + 1.5 * (h - 40)) * rate
else:
    pay = h * rate

print (pay)
