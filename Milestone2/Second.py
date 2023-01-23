

#file2 = open("Source.txt",'r')
new=open("file2.txt",'r')
s=open("sample.txt",'w')
res=open("result.txt",'w')
with open("POI.txt", 'r') as fp:
    # lines to read
    line_numbers = [10,11,12]
    # To store lines
    lines = []
    for i, line in enumerate(fp):
        # read line 4 and 7
        if i in line_numbers:
            lines.append(line.strip())
        elif i > 12:
            # don't read after line 7 to save time
            break
#print(lines)

with open('Source.txt','r') as infile, open('file2.txt', 'w') as outfile:
    copy = False
    lines3=[]
    for line in infile:
        if line.strip() == "boundary":
            copy = True
            continue
        elif line.strip() == "endel":
            copy = False
            continue
        elif copy:
            outfile.write(line)
            lines3.append(line.strip())

    
  

    i=0
    
    while(i<len(lines3)):
        l_new=lines3[i:i+3]
       # print("hii",l_new)
        for j,k in range(len(lines),len(l_new)):
               
            
                if(lines[j]!=l_new[k]):
                    
                    break
                
                elif(i==len(lines)-1 and j==len(l_new)-1):
                    res.write(lines)
                print(lines[j],end="\n")
                print(l_new[k],end="\n")
                
        i+=3    





    
                
   
   





    





