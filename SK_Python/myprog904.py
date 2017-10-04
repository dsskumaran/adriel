#fname='mbox-short.txt'
# print('Prog904')

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
dic = dict()
email_lst = list()

for line in fh:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    ls_wds = line.split(' ')
    #print(line,ls_wds)
    count = count + 1
    email_lst.append(ls_wds[1])
    if '@' not in ls_wds[1]:
        print ('Error: email without @ ', lst[1])
        quit(8)

#print("Full List", email_lst)

for eml in email_lst:
    dic[eml] = dic.get(eml,0) + 1
    #print(eml,dic[eml])

for k,v in dic.items():
    if v == max(dic.values()):
        print (k,v)