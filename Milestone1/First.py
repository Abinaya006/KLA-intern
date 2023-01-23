file = open("Format_Source.txt",'r')
file2= open("new.txt",'w')
word="boundary"
count=0
while count<=2:
    next_line = file.readline()
    
    if word in next_line:
        count+=1
    file2.write(next_line)

for line in (file.readlines() [-2:]):
    file2.write(line)
file.close()
file2.close()

