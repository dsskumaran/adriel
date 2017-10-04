def computepay(fh,fr):
    fpay = (40 + 1.5 * (fh - 40)) * fr
    return fpay
while True:
hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print('You should enter numeric value, please try again')
    quit(12)

irate = input("Enter Rate:")
rate = float(irate)
if h > 40.0:
    pay = computepay(h,rate)
else:
    pay = h * rate

print(pay)