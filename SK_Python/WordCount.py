fh = open("romeo.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count,"Lines")

#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief