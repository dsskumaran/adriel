fname='mbox-short.txt'

#fname = input("Enter file name: ")
fh = open(fname)
lst = list()
full_lst = list()
cntr=0

for line in fh:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    lst = line.split(' ')
    full_lst.append(lst[1])
    if '@' not in lst[1]:
        print ('Error: email without @ ', lst[1])
        quit(8)

while True:
    print(full_lst[cntr])
    cntr=cntr+1
    if cntr == len(full_lst) : break

#print(lst)
#full_lst.sort()
print('There were',len(full_lst),'lines in the file with From as the first word')


