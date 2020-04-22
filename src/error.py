import itertools
def ermessage(p): 
    if p==10:
         print ("ERROR::undefined symbol"),
    elif p==11:
          print ("ERROR::instruction expected"),
    elif p==12:
          print ("ERROR::,expected"),
    elif p==13:
           print("ERROR::dublication of symbol")

aa=[]
appe=[]
def comp(l,meslist,calllist):   
    for i in range(len(l)):
        c=0
        for val in calllist:
            if val not  in meslist:               
               c=c+1
            else:
               if c==i:
                    p=10                               
                    print(l[i],"         ",val,"         ",p, "          ", meslist.index(val)+1)
                    appe.append(val)
                    c=c+1
                    ermessage(p) 
#    return appe
f=open("b.asm","r")
t=f.read()
s=t.split()
line=t.split('\n')
mes=[]
bss=[]
syno=[]
sno=0
for i in range(len(s)):
    if  s[i]=="db":
       mes.append(s[i-1])
       sno=sno+1
       syno.append(sno)
   
    elif s[i]=="dd":
       mes.append(s[i-1])
       sno=sno+1
       syno.append(sno)

    elif s[i]=="dw":
       mes.append(s[i-1])
       sno=sno+1
       syno.append(sno)

    elif  s[i]=="resb":
       bss.append(s[i-1])
       sno=sno+1
       syno.append(sno)
 
    elif s[i]=="resd":
       bss.append(s[i-1])
       sno=sno+1
       syno.append(sno)

    elif  s[i]=="resw":
       bss.append(s[i-1])       
       sno=sno+1
       syno.append(sno)

#print(mes)
#print(bss)

for i in bss:
  mes.append(i)

locallist=[]
exlist=[]
ex1=[]
calllist=[]
for i in range(len(s)):
  if s[i]=="call":
    calllist.append(s[i+1])
  elif s[i]=="extern":
    exlist.append(s[i+1])
    if ',' in s[i+1]:
        ex1.append(s[i+1].split(','))      #list of list  
  elif s[i]=="jmp":
    locallist.append(s[i])
  elif s[i]=="jz":
    locallist.append(s[i])

flat=itertools.chain.from_iterable(ex1)    #list of list to list

a=list(flat)


''' line calulate length'''
linenum=[]
for i in range(len(line)):
  if "call" in line[i]:
    linenum.append(i+1)
  elif "jmp" in line[i]:
    linenum.append(i+1)
  elif "jz" in line[i]:
    linenum.append(i+1)

#print(linenum)
#print(mes)
#print(calllist)

size=len(mes)
print("             Error Table                 ")
print("")
print("Line no      Name    pointer    position in symbol ")
comp(linenum,mes,calllist)
#checking in local list
import undefine
