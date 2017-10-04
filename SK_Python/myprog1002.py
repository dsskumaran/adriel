#fname='mbox-short.txt'
print('Prog1002')

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
dic = dict()
time_lst = list()

for line in fh:
    if not line.startswith("From ") : continue
    line = line.rstrip()
    ls_wds = line.split(' ')
    tmp_time = ls_wds[6]
    ls_hrs = tmp_time.split(':')
    count = count + 1
    time_lst.append(ls_hrs[0])
    #print('Time',time_lst)

#time_lst = sorted(time_lst)

for hrs in sorted(time_lst):
    dic[hrs] = dic.get(hrs,0) + 1
    #print(hrs,dic[hrs])
tmp = list()
for hrs in dic:
    print(hrs,dic[hrs])
    #hrs_tuple = (hrs,dic[hrs])
    #tmp.append(hrs_tuple)

#print(tmp)