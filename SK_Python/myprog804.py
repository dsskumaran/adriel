fname='romeo.txt'

#fname = input("Enter file name: ")
fh = open(fname)
lst = list()
full_lst = list()
cntr=0
for line in fh:
    line = line.rstrip()
    lst = line.split(' ')
    cntr = len(lst)
    #print(cntr, lst)
    while True:
        cntr=cntr-1
        #print(cntr,lst[cntr])
        if full_lst.count(lst[cntr]) == 0:
            full_lst.append(lst[cntr])
        if cntr == 0 : break
        #print(lst)

#print(lst)
full_lst.sort()
print(full_lst)


