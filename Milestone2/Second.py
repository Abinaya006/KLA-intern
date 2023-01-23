
import math

#file2 = open("Source.txt",'r')
new=open("file2.txt",'r')
s=open("sample.txt",'w')
res=open("result.txt",'w')
with open("POI.txt", 'r') as fp:
    # lines to read
    line_numbers = [9,10,11]
    # To store lines
    lines = []
    for i, line in enumerate(fp):
        # read line 4 and 7
        if i in line_numbers:
            lines.append(line.strip())
        elif i > 12:
            # don't read after line 7 to save time
            break

dist_1=lines[2]

dist_1=dist_1[4:]


list_1 = dist_1.split()
len=list_1[0]

p1=[]
q1=[]
r1=[]
s1=[]
t1=[]
u1=[]

p1.append(int(list_1[1]))
p1.append(int(list_1[2]))

q1.append(int(list_1[3]))
q1.append(int(list_1[4]))

r1.append(int(list_1[5]))
r1.append(int(list_1[6]))

s1.append(int(list_1[7]))
s1.append(int(list_1[8]))

t1.append(int(list_1[9]))
t1.append(int(list_1[10]))

u1.append(int(list_1[11]))
u1.append(int(list_1[12]))

c1=math.dist(p1,q1)
c2=math.dist(r1,s1)
c3=math.dist(t1,u1)


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
    
      
    for i in range(0,3099,3):
        l_new=lines3[i:i+3]
      
        
        str=l_new[2]
       # print(str)
        str_new=str[4:]
        list_new = str_new.split()
        len1=list_new[0]
        if(len==len1):
      

            pp1=[]
            qq1=[]
            rr1=[]
            ss1=[]
            tt1=[]
            uu1=[]

            pp1.append(int(list_new[1]))
            pp1.append(int(list_new[2]))

            qq1.append(int(list_new[3]))
            qq1.append(int(list_new[4]))

            rr1.append(int(list_new[5]))
            rr1.append(int(list_new[6]))

            ss1.append(int(list_new[7]))
            ss1.append(int(list_new[8]))

            tt1.append(int(list_new[9]))
            tt1.append(int(list_new[10]))

            uu1.append(int(list_new[11]))
            uu1.append(int(list_new[12]))

            cc1=math.dist(pp1,qq1)
            cc2=math.dist(rr1,ss1)
            cc3=math.dist(tt1,uu1)
            
            if(c1==cc1 and c2==cc2 and c3==cc3):
                res.write("boundary\n")
                for i in l_new:
                    res.write(i+"\n")
            
                res.write("endel\n")
               

           

              

       
        



        

    
  

    




    
                
   
   





    





