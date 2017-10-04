iscore = input('Enter Score:')
try:
    score = float(iscore)
except:
    print('You should have entered a numeric value between 0 & 1')
    quit(12)

if score > 1.0:
    print('Invalid Score entered, enter between 0 & 1')
    quit(4)
elif score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'

print(grade)
