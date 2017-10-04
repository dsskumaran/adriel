# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    colpos=line.find(':')
    ex_num_str = line[(colpos+1):]
    ex_num_flo = float(ex_num_str)
    total = total + ex_num_flo
    count = count + 1

avg_flo = (total / count)
#print(count)
#print("Average spam confidence:", avg_flo)
print("Average spam confidence:", round(avg_flo,12))

#mbox-short.txt