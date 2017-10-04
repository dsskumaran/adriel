fh = open("romeo.txt", "r")

count = 0
dic = dict()

for line in fh:
    line = line.rstrip()
    ls_wds = line.split(' ')
    #print(line,ls_wds)
    count = count + 1
    for wd in ls_wds:
        dic[wd] = dic.get(wd,0) + 1
        #print(wd,dic[wd])

for k,v in dic.items():
    if v == max(dic.values()):
        print (k,v)