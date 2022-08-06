import matplotlib.pyplot as plt
import sys
opcodeA={"00000":"addf","00001":"subf","10000":"add","10001":"sub","10110":"mul","11010":"xor","11011":"or","11100":"and"} #opcodes with value as their binary code
opcodeB={"11000":"rs","11001":"ls","10010":"mov","00010":"movf"}
opcodeC={"10011":"mov","10111":"div","11101":"not","11110":"cmp"}
opcodeD={"10100":"ld","10101":"st"}
opcodeE={"11111":"jmp","01100":"jlt","01101":"jgt","01111":"je"}
opcodeF={"01010":"hlt"}

reg={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0}                               #to store values of all registers by register name
regcode={"000":"R0","001":"R1","010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}  #to get register from code
flags={"V":0,"L":0,"G":0,"E":0}         #binary flags for overflow, less than, greater than, equal 
x1=[]
y=[]
mem={}
lst=[]
def binary(x):                      #function to convert decimal to 8 bit binary
    x=int(x)
    s=bin(x)
    s=s[2::]
    while(len(s)<8):
        s="0"+s
    return s 

def binary16(x):                      #function to convert decimal to 16 bit binary
    x=int(x)
    s=bin(x)
    s=s[2::]
    while(len(s)<16):
        s="0"+s
    return s

def binary_float_16(x):
    s = get_fp(x)
    while(len(s)<16):
        s="0"+s
    return s

def binary3(x):                      #function to convert 7 bits binary to 3 bits binary
    return x[4::]

def pc_print(x):
    x=bin(x)
    x=x[2:]
    while len(x)<8:
        x="0"+x
    return x

def decTobin(s):                   #function to convert binary to decimal #NOTE: parameter must be a STRING
    return int(s,2)                  

def type(s):
    if(s in opcodeA):
        return opcodeA
    if(s in opcodeB):
        return opcodeB
    if(s in opcodeC):
        return opcodeC
    if(s in opcodeD):
        return opcodeD
    if(s in opcodeE):
        return opcodeE
    if(s in opcodeF):
        return opcodeF

def get_exp(s):
    s=float(s)
    s=int(s)
    x=bin(s)
    x=x[2::]
    n=len(x)
    n=n-1
    k=bin(n)
    k=k[2::]
    while(len(k)<3):
        k="0"+str(k)
    return k

def get_mantissa(dec, prec) :
    binary = ""
    dec=float(dec)
    int_part = int(dec)
    frac_part = dec - int_part
    while (int_part) : 
        rem = int_part % 2
        binary += str(rem)
        int_part = int_part//2
    binary = binary[ : : -1]
    binary += '.'
    while (prec) :  
        frac_part = frac_part*2
        fract_bit = int(frac_part)
        if (fract_bit == 1) :
            frac_part -= fract_bit
            binary += '1'
        else :
            binary += '0'
        prec-=1
    binary_without_point=binary.replace(".","")
    return binary_without_point[1:6:]

def get_fp(s):
    ans=get_exp(s)+get_mantissa(s,5)
    return ans

def floatingpt_to_dec(mantissa,exponent):
    num = 1
    for i in range(5):
        num += int(mantissa[i])*pow(2, -(i+1))
    
    num = num * pow(2, int(exponent,2))
    print(num)

def addf(reg3,reg2,reg1):
    reg[reg3]=reg[reg2]+reg[reg1]

def add(reg3,reg2,reg1):
    reg[reg3]=reg[reg2]+reg[reg1]

def subf(reg3,reg2,reg1):
    reg[reg3]=reg[reg2]-reg[reg1]

def sub(reg3,reg2,reg1):
    reg[reg3]=reg[reg2]-reg[reg1]

def mul(reg3,reg2,reg1):
    reg[reg3]=reg[reg2]*reg[reg1]

def movf(reg1,imm):       #imm is in decimal
    reg[reg1]=imm

def movf2(reg1, imm):
    reg[reg1]=imm

def xor(reg3,reg2,reg1):
    reg[reg3]=reg[reg2]^reg[reg1]

def OR(reg3,reg2,reg1):
    reg[reg3]=reg[reg2] | reg[reg1]

def AND(reg3,reg2,reg1):
    reg[reg3]=reg[reg2] & reg[reg1]

def div(reg2,reg1):
    reg["R0"]=reg[reg2]/reg[reg1]
    reg["R1"]=reg[reg2]%reg[reg1]

def invert(reg2,reg1):
    z=""
    yz=binary16(reg[reg1])
    yz=str(yz)
    for i in yz:
        if i=="0":
            z+="1"
        else:
            z+="0"
    binary =int(z)
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    reg[reg2]=decimal

def cmp(reg2,reg1):
    a=reg[reg2]
    b=reg[reg1]
    flags["L"]= a<b
    flags["G"]= a>b
    flags["E"]= a==b

def ls(reg1,imm):                #imm is in decimal
    reg[reg1]<<=imm

def rs(reg1,imm):                #imm is in decimal
    reg[reg1]>>=imm

def printout(pc):
    print(pc_print(pc),end=" ")
    if type(reg['R0']) == float:
        print(binary_float_16(reg['R0']), end =" ")
    else:
        print(binary16(reg['R0']), end =" ")
    if type(reg['R1']) == float:
        print(binary_float_16(reg['R1']), end =" ")
    else:
        print(binary16(reg['R1']), end =" ")
    if type(reg['R2']) == float:
        print(binary_float_16(reg['R2']), end =" ")
    else:
        print(binary16(reg['R2']), end =" ")
    if type(reg['R3']) == float:
        print(binary_float_16(reg['R3']), end =" ")
    else:
        print(binary16(reg['R3']), end =" ")
    if type(reg['R4']) == float:
        print(binary_float_16(reg['R4']), end =" ")
    else:
        print(binary16(reg['R4']), end =" ")
    if type(reg['R5']) == float:
        print(binary_float_16(reg['R5']), end =" ")
    else:
        print(binary16(reg['R5']), end =" ")
    if type(reg['R6']) == float:
        print(binary_float_16(reg['R6']), end =" ")
    else:
        print(binary16(reg['R6']), end =" ")
    print("000000000000", end="")
    print(flags["V"],end="")
    print(flags["L"],end="")
    print(flags["G"],end="")
    print(flags["E"])

def memorydump():
    count=0
    for i in instructions:
        if(not(i and i.strip())):
            continue
        print(i)
        count=count+1
    i=0
    while(i!=len(mem)):
        x=mem[str(pc_print(count))]
        print(binary16(x))
        count=count+1
        i=i+1
    while(count!=256):
        print("0000000000000000")
        count=count+1

def freset():
    for i in flags:
        flags[i]=0
def bindec(yy):
    yy=str(yy)
    binary=int(yy)
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal
#f=open("input.txt","r")
f=sys.stdin.read()
instructions=f.split("\n")
halt=False
pc=-1
reset=0
cycle=-1
while halt==False:
    f=0
    check=0
    cycle=cycle+1
    if reset==1:
        pc+=1
        i=instructions[pc]
        op=i[0:5]
        if op in opcodeA:
            y.append(pc)
            reg1=regcode[i[7:10]]
            reg2=regcode[i[10:13]]
            reg3=regcode[i[13:16]]
            if(binary16(reg[reg1])=="0000000000000000"):
                f=1
            if opcodeA[op]=="add":
                add(reg3,reg2,reg1)
                if(reg[reg3]<0)or(reg[reg3]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg3]<0: 
                        reg[reg3]=0
                    elif reg[reg3]>((2**16)-1):
                        reg[reg3]=reg[reg3]%((2**16)-1)
                    if binary16(reg[reg3])=="0000000000000000" and reg[reg3]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            elif opcodeA[op]=="sub":
                sub(reg3,reg1,reg2)
                if(reg[reg3]<0)or(reg[reg3]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg3]<0: reg[reg3]=0
                    if binary16(reg[reg3])=="0000000000000000" and reg[reg3]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            elif opcodeA[op]=="addf":
                addf(reg3,reg2,reg1)
                if reg[reg3] >= 1 and reg[reg3] <= 252:
                    flags['V'] = 0
                else:
                    flags['V'] = 1
                    reg[reg3] = 252.0
                    reset=1
            elif opcodeA[op]=="subf":
                subf(reg3,reg2,reg1)
                if reg[reg3] < 0:
                    reg[reg3] = 0.0
                    flags['V'] = 1
                    reset=1
                else:
                    flags['V'] = 0
            elif opcodeA[op]=="mul":
                mul(reg3,reg2,reg1)
                if(reg[reg3]<0)or(reg[reg3]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg3]<0:
                        reg[reg3]=0
                    elif reg[reg3]>((2**16)-1):
                        reg[reg3]=reg[reg3]%((2**16)-1)
                    if binary16(reg[reg3])=="0000000000000000" and reg[reg3]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            elif opcodeA[op]=="xor":
                xor(reg3,reg2,reg1)
            elif opcodeA[op]=="or":
                OR(reg3,reg2,reg1)
            elif opcodeA[op]=="and":
                AND(reg3,reg2,reg1)
        elif op in opcodeB:
            y.append(pc)
            reg1=regcode[i[5:8]]
            if(binary16(reg[reg1])=="0000000000000000"):
                f=1
            immediate=int(bindec(i[8:16]))
            if opcodeB[op]=="mov":
                movf(reg1,immediate)
                if(reg[reg1]<0)or(reg[reg1]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg1]<0:reg[reg1]=0
                    if binary16(reg[reg1])=="0000000000000000" and reg[reg1]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            if opcodeB[op]=="movf":
                movf2(reg1, immediate)
                if(reg[reg1]<1)or(reg[reg1]>252):
                    flags["V"]=1
                    if reg[reg1]<1:
                        reg[reg1] = 0.0
                    elif reg[reg1]>252:
                        reg[reg1] = 252.0
                    reset=1
            elif opcodeB[op]=="rs":
                ls(reg1,immediate)
            elif opcodeB[op]=="ls":
                rs(reg1,immediate)
        elif op in opcodeC:
            y.append(pc)
            reg1=regcode[i[10:13]]
            reg2=regcode[i[13:16]]
            if opcodeC[op]=="mov":
                if reg1=="FLAGS":
                    reg[reg2]=flags["E"]+flags["G"]+flags["L"]+flags["V"]
                else:
                    reg[reg2]=reg[reg1]
            elif opcodeC[op]=="div":
                div(reg2,reg1)
            elif opcodeC[op]=="not":
                invert(reg2,reg1)
            elif opcodeC[op]=="cmp":
                p=reg[reg1]
                q=reg[reg2]
                if p==q:
                    flags["E"]=1
                    reset=1
                elif(p>q):
                    flags["G"]=1
                    reset=1
                elif(p<q):
                    flags["L"]=1
                    reset=1
        elif op in opcodeD:
            reg1=regcode[i[5:8]]
            adr=i[8:16]
            adrr=adr
            y.append(bindec(adr))
            y.append(pc)
            x1.append(cycle)
            if opcodeD[op]=="ld":
                if adr not in mem:
                    reg[reg1]=0
                else:
                    reg[reg1]=mem[adrr]
            elif opcodeD[op]=="st":
                mem[adrr]=reg[reg1]
        elif op in opcodeE:
            adr=i[8:16]
            y.append(bindec(adr))
            y.append(pc)
            x1.append(cycle)
            if opcodeE[op]=="jmp":
                freset()
                printout(pc)
                check+=1
                pc=bindec(adr)
                pc=pc-1
            elif opcodeE[op]=="jlt":
                if flags["L"]>0:
                    freset()
                    printout(pc)
                    check+=1
                    pc=bindec(adr)
                    pc=pc-1
            elif opcodeE[op]=="jgt":
                if flags["G"]>0:
                    freset()
                    printout(pc)
                    check+=1
                    pc=bindec(adr)
                    pc=pc-1
            elif opcodeE[op]=="je":
                if flags["E"]>0:
                    check+=1
                    freset()
                    printout(pc)
                    pc=bindec(adr)
                    pc=pc-1
        elif op in opcodeF:
            y.append(pc)
            halt=True
            printout(pc)

        for i in flags:
            flags[i]=0
        if (op not in opcodeF) and (check<1):
            printout(pc)
        reset=0
    else:
        reset=0
        for i in flags:
            flags[i]=0
        pc+=1
        i=instructions[pc]
        op=i[0:5]
        if op in opcodeA:
            y.append(pc)
            reg1=regcode[i[7:10]]
            reg2=regcode[i[10:13]]
            reg3=regcode[i[13:16]]
            if(binary16(reg[reg3])=="0000000000000000"):
                f=1
            if opcodeA[op]=="add":
                add(reg3,reg2,reg1)
                if(reg[reg3]<0)or(reg[reg3]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg3]<0:
                        reg[reg3]=0
                    elif reg[reg3]>((2**16)-1):
                        reg[reg3]=reg[reg3]%((2**16)-1)
                    if binary16(reg[reg3])=="0000000000000000" and reg[reg3]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            elif opcodeA[op]=="sub":
                sub(reg3,reg1,reg2)
                if(reg[reg3]<0)or(reg[reg3]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg3]<0:
                        reg[reg3]=0
                    if binary16(reg[reg3])=="0000000000000000" and reg[reg3]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            elif opcodeA[op]=="addf":
                addf(reg3,reg2,reg1)
                if reg[reg3] >= 1 and reg[reg3] <= 252:
                    flags['V'] = 0
                else:
                    flags['V'] = 1
                    reg[reg3] = 252.0
                    reset=1
            elif opcodeA[op]=="subf":
                subf(reg3,reg2,reg1)
                if reg[reg3] < 0:
                    reg[reg3] = 0.0
                    flags['V'] = 1
                    reset=1
                else:
                    flags['V'] = 0            
            elif opcodeA[op]=="mul":
                mul(reg3,reg2,reg1)
                if(reg[reg3]<0)or(reg[reg3]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg3]<0:
                        reg[reg3]=0
                    elif reg[reg3]>((2**16)-1):
                        reg[reg3]=reg[reg3]%((2**16)-1)
                    if binary16(reg[reg3])=="0000000000000000" and reg[reg3]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            elif opcodeA[op]=="xor":
                xor(reg3,reg2,reg1)
            elif opcodeA[op]=="or":
                OR(reg3,reg2,reg1)
            elif opcodeA[op]=="and":
                AND(reg3,reg2,reg1)
        elif op in opcodeB:
            y.append(pc)
            reg1=regcode[i[5:8]]
            if(binary16(reg[reg1])=="0000000000000000"):
                f=1
                immediate=int(bindec(i[8:16]))
            if opcodeB[op]=="mov":
                movf(reg1,immediate)
                if(reg[reg1]<0)or(reg[reg1]>((2**16)-1)):
                    flags["V"]=1
                    if reg[reg1]<0:
                        reg[reg1]=0
                    if binary16(reg[reg1])=="0000000000000000" and reg[reg1]!=0 and f==1:
                        flags["V"]=0
                    reset=1
            if opcodeB[op]=="movf":
                movf2(reg1, immediate)
                if(reg[reg1]<1)or(reg[reg1]>252):
                    flags["V"]=1
                    if reg[reg1]<1:
                        reg[reg1] = 0.0
                    elif reg[reg1]>252:
                        reg[reg1] = 252.0
                    reset=1
            elif opcodeB[op]=="rs":
                rs(reg1,immediate)
            elif opcodeB[op]=="ls":
                ls(reg1,immediate)
        elif op in opcodeC:
            y.append(pc)
            reg1=regcode[i[10:13]]
            reg2=regcode[i[13:16]]
            if opcodeC[op]=="mov":
                if reg1=="FLAGS":
                    reg[reg2]=flags["E"]+flags["G"]+flags["L"]+flags["V"]
                else:
                    reg[reg2]=reg[reg1]
            elif opcodeC[op]=="div":
                reg["R0"]=reg[reg1]/reg[reg2]
                reg["R1"]=reg[reg1]%reg[reg2]
            elif opcodeC[op]=="not":
                invert(reg2,reg1)
            elif opcodeC[op]=="cmp":
                p=reg[reg1]
                q=reg[reg2]
                if p==q:
                    flags["E"]=1
                    reset=1
                elif(p>q):
                    flags["G"]=1
                    reset=1
                elif(p<q):
                    flags["L"]=1
                    reset=1
        elif op in opcodeD:
            reg1=regcode[i[5:8]]
            adr=i[8:16]
            y.append(bindec(adr))
            y.append(pc)
            x1.append(cycle)
            if opcodeD[op]=="ld":
                if adr not in mem:
                    mem[adr]=0
                reg[reg1]=mem[adr]
            elif opcodeD[op]=="st":
                mem[adr]=reg[reg1]
        elif op in opcodeE:
            adr=i[8:16]
            y.append(bindec(adr))
            y.append(pc)
            x1.append(cycle)
            if opcodeE[op]=="jmp":
                printout(pc)
                pc=bindec(adr)
            elif opcodeE[op]=="jlt":
                if flags["L"]>0:
                    printout(pc)
                    pc=bindec(adr)
            elif opcodeE[op]=="jgt":
                if flags["G"]>0:
                    printout(pc)
                    pc=bindec(pc)
            elif opcodeE[op]=="je":
                if flags["E"]>0:
                    printout(pc)
                    pc=bindec(pc)
        elif op in opcodeF:
            y.append(pc)
            halt=True
            printout(pc)
        
        if op not in opcodeF:
            printout(pc)
    x1.append(cycle)
memorydump()
#plt.scatter(x1, y, c="blue")
#plt.show()


