from os import system
import math

d={"b":1,"B":8,"Kb":1000,"KB":8000,"Mb":1000000,"MB":8000000,"Gb":1000000000,"GB":8000000000}
tags =["B","KB","MB","GB","TB"]
def convert(B):
    i=0
    next_B=B
 
    while (i<len(tags)and B >= 1024):
            next_B=B/1024.0
            i=i+1
            B=B/1024
 
    return str(round(next_B, 2))+" "+tags[i]

def bits(s):
    n=0
    s=s.strip()
    for i in range(0,len(s),1):
        if not s[i].isnumeric():
            n=i
            break
    pre=int(s[0:n])
    post=s[n::]
    return pre*d[post]


space=input("Enter the Total Space in Memory (e.g 16Mb or 8MB): ")
print('''\nChoose a Type of Addressable Memory:
  
         1. Bit Addressable Memory - Cell Size = 1 bit
         2. Nibble Addressable Memory - Cell Size = 4 bit
         3. Byte Addressable Memory - Cell Size = 8 bits
         4. Word Addressable Memory - Cell Size = Word Size
         5. Default \n''')
mem=int(input("Enter option number: "))

if mem==1:
    mem=1
elif mem==2:
    mem=4
elif mem==3 or mem==5:
    mem=8
elif mem==4:
    mem=int(input("Enter the bits of the CPU: "))            

print('''\nChoose a type of query: 

            1. ISA Related
            2. System Enhancement Related\n''')
query=int(input("Enter Query: "))            

def A(l,r):
    address=bits(space)/mem
    address=round(math.log2(address))
    print(f"\nAn Address in this ISA is represented by: {address} bits")
    op=l-r-address
    print(f"Number of bits needed by the OP Code is: {op} bits")
    filler=l-r-r-op
    print(f"Number of Filler bits in Type B is: {filler} bits")
    number=2**op
    print(f"Maximum number of Instructions this ISA can support is: {number}")
    print(f"Maximum number of Registers this ISA can support is: {2**r}")

def t1():
    cpu=int(input("Enter the bits of the CPU: "))
    print('''\nChoose a Type of Addressable Memory:
  
         1. Bit Addressable Memory - Cell Size = 1 bit
         2. Nibble Addressable Memory - Cell Size = 4 bit
         3. Byte Addressable Memory - Cell Size = 8 bits
         4. Word Addressable Memory - Cell Size = Word Size \n''')
    m=int(input("Enter option number: "))
    if m==1:
        m=1
    elif m==2:
        m=4
    elif m==3:
        m=8
    elif m==4:
        m=cpu
    address=bits(space)/mem
    address=round(math.log2(address))
    newadd=bits(space)/m
    newadd=round(math.log2(newadd))
    print(newadd-address)


def t2():
    cpu=int(input("Enter the bits of the CPU: "))
    pins=int(input("Enter the Number of Address pins: "))
    print('''\nChoose a Type of Addressable Memory:
  
         1. Bit Addressable Memory - Cell Size = 1 bit
         2. Nibble Addressable Memory - Cell Size = 4 bit
         3. Byte Addressable Memory - Cell Size = 8 bits
         4. Word Addressable Memory - Cell Size = Word Size \n''')
    m=int(input("Enter option number: "))
    if m==1:
        m=1
    elif m==2:
        m=4
    elif m==3:
        m=8
    elif m==4:
        m=cpu
    b=2**pins
    b=b*m
    print(convert(b/8))    

if(query==1):
    l=int(input("\nEnter the Length of the instruction in BITS: "))
    r=int(input("Enter the Length of the register in BITS: "))
    A(l,r)
elif(query==2):
    print('''\nChoose a Type:
  
         1. Type 1
         2. Type 2 \n''')
    t=int(input("Enter: "))
    if(t==1):
        t1()
    else:
        t2()    

