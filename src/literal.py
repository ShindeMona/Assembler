def dec(dec):
    decimal = int(dec)
    # Prints equivalent decimal
    return "{0:X}".format(decimal)

f=open("b.asm","r")
t=f.read()
s=t.split()
mes=[]
bss=[]
size=[]
k=[]
k1=[]
entry=1
ent=[]
si=0
for i in range(len(s)):
    if  s[i]=="db":
       mes.append(s[i+1])
       ent.append(entry)
       #print(s[i-1])
       entry=entry+1   
       size.append(1)
         
    elif s[i]=="dd":
       mes.append(s[i+1])
       ent.append(entry)
       entry=entry+1
       #print(s[i])
       size.append(4)
       k.append(s[i+1])
     
    elif  s[i]=="dw":
       mes.append(s[i+1])
       ent.append(entry)
       entry=entry+1
       #rint(s[i-1])
       size.append(2)
       k.append(s[i+1])

    elif  s[i]=="resb":
       bss.append(s[i+1])
       ent.append(entry)
       entry=entry+1
       size.append(1*int(s[i+1]))
       k1.append(s[i+1])

    elif  s[i]=="resd":
       bss.append(s[i+1])
       ent.append(entry)
       entry=entry+1
       size.append(8*int(s[i+1]))
       k1.append(s[i+1])
            
    elif s[i]=="resw":
       bss.append(s[i+1])
       ent.append(entry)
       entry=entry+1
       size.append(2*int(s[i+1]))
       k1.append(s[i+1])
       
#print(mes)
for i in bss:
   mes.append(i)
#print(mes)
'''hex code'''
for i in range(len(s)):
     if s[i]=="db":
         st=s[i+1]

lis=list(st)
#print(lis)
l=0
hexd=[]
hexd2=[]
for i in range(len(k)):
    hexd.append(dec(k[i]))
    
for i in range(len(k1)):
    hexd2.append(dec(k1[i]))
   
asc=[]
# print ascii value
#print("ascii value")
for i in range(len(lis)):
        asc.append(ord(lis[i]))

#print("ASCII")
#print(asc)
#print("HEX VALUES")

final=[]
for i in range(len(asc)):

    final.append(dec(asc[i]))
#print(final)
hexd.append(final)

for i in hexd2:
   hexd.append(i)
#print("final")
#print(hexd)

print("                                      Literal Table                                    ")
print("")
print("")
print("Entry No      String/int                 Hex                                              size")
for i in range(len(mes)):
  print(ent[i],"|          ",mes[i],"|                      ",hexd[i],"|                                             ",size[i],"|")


