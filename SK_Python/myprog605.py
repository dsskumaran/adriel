#       ----|----1----|----2----|----3----|
text = "X-DSPAM-Confidence:    0.8475";

dotpos=text.rfind(' ')
#print(dotpos)
extr_num_str = text[(dotpos+1):(dotpos+10)]
#print(extr_num_str)
extr_num_flo = float(extr_num_str)
#print(extr_num_flo)


colpos=text.find(':')
ex_num_str = text[(dotpos+1):]
#print(ex_num_str)
ex_num_flo = float(ex_num_str)
print(ex_num_flo)