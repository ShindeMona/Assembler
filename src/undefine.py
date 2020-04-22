
'''
THIS CODE GIVE AN ERROR WHEN WE CALL A FUNCTION AND NOT DECLARATION IN EXTERN AND CHECK LOCAL DEFINATION 
'''
import itertools
def ermessage(p):
    if p==10:
         print ("ERROR::undefined symbol"),
    elif p==11:
          print ("ERROR::expression syntax error"),
    elif p==12:
          print ("ERROR::,expected"),
    elif p==13:
           print("ERROR::dublication of symbol")

aa=[]
appe=[]
app=[]
def comp(l,exlist1, callist2):
    for i in range(len(l)):
        c=0 
        for val in callist2:
            if val not in exlist1 :
     
                  if i==c:
                      p=10
                      print(l[i],"         ",val,"         ",p, "          ", callist2.index(val)+1)
                      appe.append(val)  
                      c=c+1
                      ermessage(p)                         
            else:
                  aa.append(val)
   
def checklocal(l,jmplist,localdef):
  for i in range(len(l)):
     c=0
     for val in jmplist:
         if val in localdef:         
            c=c+1
         else:         
            if i==c:
                p=11
                print(l[i],"         ",val,"         ",p, "          ", jmplist.index(val)+1)
                app.append(val)
                c=c+1
                ermessage(p)

fi=open("b.asm","r")
t=fi.read()
s=t.split()
#print(s)
sys1=[]
sys=[]
pus=[]
for i in range(len(s)):
   if "call" in s[i]:
      sys.append(s[i+1])            
   elif "extern" in s[i]:
      sys1.append(s[i+1])   
   elif "jmp" in s[i]:
      pus.append(s[i+1])


#print("\n push :",pus)
#comp(sys1,sys)
ap=[]
for i in range(len(s)):
    if ","in s[i]:
        ap.append(s[i])

pt=[]
for i in range(len(ap)):
    if','in ap[i]:
     pt.append ((ap[i]).split(','))

 
#print(pt)
#print("now list")

flat=itertools.chain.from_iterable(pt)

a=list(flat)
#print(a)

for i in a : 
    sys1.append(i) 
#print(sys1)
#print(appe)

fp=open("b.asm","r")
tp=fp.read()
sp=tp.split('\n')
lino=[]
call=[]
local=[]
for i in range(len(sp)):
    if "call" in sp[i]:
        call.append((sp[i]).split(' '))
        lino.append(i+1)
for i in range(len(s)):
    if s[i].endswith(':'):
        local.append(s[i].replace(':',''))
        
#print("\n local",local)
#print("jmp",pus)
lo=[]
for i in range(len(sp)):   
     if "jmp" in sp[i]:
           lo.append(i+1)          
#print(call)   
#print(lino)
#print(lo)
comp(lino,sys1,sys)
checklocal(lo,pus,local)
