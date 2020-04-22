import itertools
f=open("b.asm","r")
t=f.read()
s=t.split()
line=t.split('\n')
#print(s)
ins=[]
oprand=[]
opname=[]
lineno=[]
op=[]
op1=[]
op2=[]
op3=[]
op4=[]
op5=[]
op6=[]
op7=[]
op8=[]
op11=[]
op22=[]
linenumber=[]
size=[]

for i in range(len(s)):
     if  s[i]=="inc":
        ins.append("inc")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op1.append(s[i+1].split(','))
           import itertools
           flat=itertools.chain.from_iterable(op1)# convert list of list to list
           a1=list(flat)
           op11.append(a1[0])
           op22.append(a1[1])
           
        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")
           size.append(1)
     elif  s[i]=="jmp":
        ins.append("jmp")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op2.append(s[i+1].split(','))
           import itertools
           flat=itertools.chain.from_iterable(op2)# convert list of list to list
           a2=list(flat)
           op11.append(a2[0])
           op22.append(a2[1])

        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-") 
           size.append(5)


     elif  s[i]=="mov":
        ins.append("mov")        
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op3.append(s[i+1].split(','))           
           flat=itertools.chain.from_iterable(op3)# convert list of list to list
           a3=list(flat)
           op11.append(a3[0])
           op22.append(a3[1])
           size.append(4)
        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")

     elif s[i]=="add":
        ins.append("add")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op4.append(s[i+1].split(','))          
           flat=itertools.chain.from_iterable(op4)# convert list of list to list
           a4=list(flat)
           op11.append(a4[0])
           op22.append(a4[1])
           size.append(1)

        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")

     elif  s[i]=="jz":
        ins.append("jz")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op5.append(s[i+1].split(','))
           flat=itertools.chain.from_iterable(op5)# convert list of list to list
           a5=list(flat)
           op11.append(a5[0])
           op22.append(a5[1])

        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")
           size.append(1)

     elif  s[i]=="comp":
        ins.append("jz")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op6.append(s[i+1].split(','))
           flat=itertools.chain.from_iterable(op6)# convert list of list to list
           a6=list(flat)
           op11.append(a6[0])
           op22.append(a6[1])
           size.appned(4)
        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")
           size.append(4)

     elif  s[i]=="push":
        ins.append("push")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op7.append(s[i+1].split(','))
           flat=itertools.chain.from_iterable(op7)# convert list of list to list
           a7=list(flat)
           op11.append(a7[0])
           op22.append(a7[1])

        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")
           size.append(2)
  
     elif  s[i]=="push":
        ins.append("call")
        oprand.append(s[i+1])
        if ',' in s[i+1]:
           op.append(2)
           op8.append(s[i+1].split(','))
           flat=itertools.chain.from_iterable(op8)# convert list of list to list
           a8=list(flat)
           op11.append(a8[0])
           op22.append(a8[1])

        else:
           op.append(1)
           op11.append(s[i+1])
           op22.append("-")
           size.append(2)

''' calculate line number'''

for i in range(len(line)):
    for val in ins:
         if val in line[i]:
            i=i+1
            linenumber.append(i)
num=1
print("\n                 opcode Table  \n\n ")
print("no |line| name of ins. | no_of_oprand        |          oprand1 |          oprand2 |       code  | size |")
for i in range(len(oprand)):
    print(num,"  ",linenumber[i],"  ",ins[i],"          ",op[i],"                   ",op11[i],"                     ",op22[i] ,"                    ",size[i])
    num=num+1             

                            
