#fhand = open('mbox-short.txt')
#for line in fhand:
#    if line.startswith('From:') :
#        print(line)


fhand = open('mbox-short.txt')
for line in fhand:
#    line = line.rstrip()
    line = fhand.read()
    if not '@uct.ac.za' in line :
        continue
    print(line)
