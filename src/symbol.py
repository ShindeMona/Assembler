import itertools
from string import digits
#symbol table
f=open("b.asm","r")
t=f.read()
s=t.split()
line=t.split('\n')
mes=[]
bss=[]
adddata=0
addbss=0
addb=[]
address=[]
datasection=[]
bssection=[]
le=0         #start len of db
sizeofins=[]
lenth=0
lenw=0
lenresb=0
lenresw=0
lenres=[]
countdata=[]
countdd=0
countdw=0
countresb=0
countresd=0
count=0
no_of_element=[]
add_address=[]
for i in range(len(s)):
    if  s[i]=="db":
      mes.append(s[i-1])    
      address.append(adddata)
      adddata=adddata+1
      datasection.append("d")
      le=le+1
      sizeofins.append(le)
      count=count+1
      countdata.append(count)
      no_of_element.append(1)
      
    elif s[i]=="dd":
       mes.append(s[i-1])
       address.append(adddata)
       adddata=adddata+4
       datasection.append("d")
       lenth=4
       sizeofins.append(lenth)
       countdd=countdd+1
       countdata.append(countdd)
       no_of_element.append(1)
 
    elif  s[i]=="dw":
       mes.append(s[i-1])
       address.append(adddata)
       adddata=adddata+8
       datasection.append("d")
       lenw=8
       sizeofins.append(lenw)
       no_of_element.append(1)

    elif s[i]=="resb":
       bss.append(s[i-1])
       addb.append(addbss)
       addbss=addbss+int (s[i+1])
       bssection.append("b")
       lenofb=1
       lenres.append(lenofb)    
       no_of_element.append(1)

    elif s[i]=="resd":
       bss.append(s[i-1])
       addb.append(addbss)
       bssection.append("b")
       lenres.append(4)
       addbss=addbss+(4*int (s[i+1]))
       no_of_element.append(1)

    elif s[i]=="resw":
       bss.append(s[i-1])
       addb.append(addbss)
       addbss=addbss+(2*int (s[i+1]))
       bssection.append("b")
       lenres.append(8)
       no_of_element.append(1)

if "main:"in mes:
  mes.remove("main:")
for i in bss:
   mes.append(i)

comma=[]
for i in range(len(s)):        
   if ',' in s[i]:
     comma.append(s[i])

dlist=[]
for i in range(len(comma)):
      dlist.append(comma[i].split(',')) # make list of list by spliting by comma

fl=itertools.chain.from_iterable(dlist)  #convert list of list to single list
a=list(fl)

for i in range(len(a)):                    #remove registors
    if "eax" in a:
       a.remove("eax")
    elif "ecx" in a:
       a.remove("ecx")
    elif "edx" in a:
       a.remove("edx")
    elif "esp" in a:
       a.remove("esp")
    elif "ebp" in a:
       a.remove("ebp")
    elif "esi" in a:
       a.remove("esi")
    elif "edi" in a:
       a.remove("edi")
    elif "ebx" in a:
       a.remove("ebx")

unsymbol=[]
symbol=[]
for val in a:                                  #check for each value in no_int which present in decation of symbol ie data and bss section
   if val in mes:
      symbol.append(val)      
   else:
     unsymbol.append(val)
 
u=[x for x in unsymbol if not x.isdigit()]

if '' in u:
   u.remove('');                                          # getting external function defination name

''' check symbol is external function or local label'''
l=[]
ad2=0
locallabel=[]
localadd=[]
textsection=[]
text=[]
for i in range(len(s)):
   if s[i].endswith(':'):                                   #collect local defination of label
       l.append(s[i])
       localadd.append(ad2)
       textsection.append("T")
       text.append("-")

for z in range(len(l)):
    if( l.count(l[z]))>1:
        print(l[z],":error defination of label should not  shoud not more than 1")
  
for i in range(len(l)):    
   locallabel.append(l[i].replace(':',''))                 #remove : from local labels

                                                           #merging locallabel and symbol for symbol by making copy
syscopy= mes.copy()
localcopy=locallabel.copy()
for i in localcopy:                                        #finally getting all symbols from table
    syscopy.append(i)

for i in u:
   syscopy.append(i)                                       # symbol
jmpins=[]
callins=[]
for i in range(len(s)):
    if s[i]=="jmp":
       jmpins.append(s[i+1])
       textsection.append("T")
       text.append("-")
    elif  s[i]=="call":
       callins.append(s[i+1])
       
#extern symbol collection codding here start
line=t.split('\n')
exlist=[]
exadd=[]
addofex=0
for i in range(len(line)):
     if "extern" in line[i]:
         exlist.append(line[i])
ex=[]
for i in range(len(exlist)):
   ex.append(exlist[i].split(' '))
f=itertools.chain.from_iterable(ex)                       #convert list of list to single list
externlist=list(f)
for i in range(len(externlist)):
   if '' in externlist:
     externlist.remove('')
   elif "extern" in externlist:
     externlist.remove("extern")
ex2=[]
for i in range(len(externlist)):
  ex2.append(externlist[i].split(','))
  textsection.append("T")
  text.append("-")
  
externlistfinal=[]
z=itertools.chain.from_iterable(ex2)                    #convert list of list to single list
externlistfinal=list(z)

for i in range(len(externlistfinal)):
   no_of_element.append(1)

for i in range(len(externlistfinal)):
         exadd.append(addofex)

'''
adding all adresss of data bss and text into adress by appending
'''
for i in addb:
   address.append(i)
for i in localadd:
   address.append(i)
for i in exadd:
   address.append(i)
for i in bssection:
    datasection.append(i)
for i in textsection:
    datasection.append(i)

for i in lenres:
   sizeofins.append(i)
for i in text:
   sizeofins.append(i)

de='d'
sym=[]
res=[]
lenp=[]
list1=[]
for i in range(len(s)):
   if "dd" in s[i]:
        sym.append(s[i-1]) 
   elif "db" in s[i]:
        sym.append(s[i-1])
   elif "dw" in s[i]:
        sym.append(s[i-1])   
   elif "resw" in s[i]:
        res.append(s[i-1])    
   elif "resd" in s[i]:
       res.append(s[i-1])
   elif "resb" in s[i]:
       res.append(s[i-1])

for i in range(len(sym)):
   list1.append("D")
for i in range(len(res)):
   list1.append("D")

for i in range(len(s)):
    if s[i].endswith(':'):   
        lenp.append(s[i])

size=[]
for i in range(len(lenp)):
    size.append(lenp[i].replace(':', ''))   
    no_of_element.append(1)

for i in range(len(size)):                            # print text section
    list1.append("D")

callist=[]
exlist=[]
for i in range(len(s)):
   if "extern" in s[i]:
      exlist.append(s[i+1])
   elif "call" in s[i]:
      callist.append(s[i+1])

x=[]
for i in range(len(exlist)):
      x.append(exlist[i].split(','))

fl=itertools.chain.from_iterable(x)                   #convert list of list to single list
ex=list(fl)

for val  in ex:
    list1.append("U") 

#print("final list")
print("\n\t\t SYMBOL TABLE:\n")
print("")
print("\n Name:",syscopy)
print("\n address",address)
print("\n section",datasection)
print("\n size",sizeofins)
print("\n Noofelement",no_of_element)
print("\n D/U",list1)
