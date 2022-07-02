from os import system
import sys
system("cls")
final=[]
def binary(x):                      #function to convert decimal to 8 bit binary
    x=int(x)
    s=bin(x)
    s=s[2::]
    while(len(s)<8):
        s="0"+s
    return s    

opcodeA={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"} #opcodes with value as their binary code
opcodeB={"rs":"11000","ls":"11001","mov":"10010"}
opcodeC={"mov":"10011","div":"10111","not":"11101","cmp":"11110"}
opcodeD={"ld":"10100","st":"10101"}
opcodeE={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}
opcodeF={"hlt":"01010"}
reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
flags={"V":"0","L":"0","G":"0","E":"0"}
pc=0                                             #execution line number
count=0
with open("input.txt","r") as f:                 #reading assembly code from input file to count lines
    instructions=f.read()
    instructions=instructions.split("\n")
    for line in instructions:                   #reading file line by line
        if len(line)!=0:
            if line.split()[0]=="var":
                continue
        elif len(line)==0:
            continue
        else:
            pc+=1
def type(pc,l):
    if l.split()[0] in opcodeA.keys():
        return opcodeA
    elif l.split()[0] in opcodeB.keys() and l.split()[2][0]=="$":
        return opcodeB
    elif l.split()[0] in opcodeC.keys():
        return opcodeC
    elif l.split()[0] in opcodeD.keys():
        return opcodeD
    elif l.split()[0] in opcodeE.keys():
        return opcodeE
    elif l.split()[0] in opcodeF.keys():
        return opcodeF
    else:
        print("Line No:" +str(pc)+" Instruction is Invalid")
        sys.exit()
'''
def register(pc,r):
    if r in reg.keys:
        return reg[r]
    else:
        print("Line No: "+str(pc)+" register doesn't exist")
        sys.exit()
'''
labels={}
variables={}
lines=0
#labels
for i in instructions:
    if len(i.split())==0:
        continue
    if ":" in i.split()[0]:
        if (i.split()[0][:-1] in opcodeA.keys()) or (i.split()[0][:-1] in opcodeB.keys()) or (i.split()[0][:-1] in opcodeC.keys()) or (i.split()[0][:-1] in opcodeD.keys()) or (i.split()[0][:-1] in opcodeE.keys()) or (i.split()[0][:-1] in opcodeF.keys()):
            print("Instruction cannot be used as Label")
            sys.exit()
        labels[i.split()[0][:-1]]=binary(lines)
        lines+=1
    if i.split()[0]!="var" and i.split()[0]!="":
        lines+=1
#variables
for i in instructions:
    if len(i.split())==0:
        continue
    if i.split()[0]=="var":
        if len(i.split())!=2:
            print("No Variable Name given")    
            sys.exit()
        if i.split()[1].isalnum()==False:
            print("Line no: "+str(pc)+" variable names can only by alphanumeric")
            sys.exit()
        if (i.split()[1]=="var") or (i.split()[1] in labels.keys()) or (i.split()[1] in opcodeA.keys()) or (i.split()[1] in opcodeB.keys()) or (i.split()[1] in opcodeC.keys()) or (i.split()[1] in opcodeD.keys()) or (i.split()[1] in opcodeE.keys()) or (i.split()[1] in opcodeF.keys()):
            print("Invalid Variable Name")
            sys.exit()
        variables[i.split()[1]]=str(binary(lines))
        lines+=1
#misuse error
for lab in labels:
    if lab in variables:
        print("Misuse of labels as variables or vice-versa")
        sys.exit()
#halt error checks
temp=[]
for i in instructions:
    if i!="":
        temp.append(i)
if temp[-1].split()[0]!="hlt":
        print("Halt not used at the end")
        sys.exit()
for i in range(0,len(instructions)-1):
    if instructions[i]!="":
        if instructions[i].split()[0]=="hlt":
            print("Halt used before last line")
            sys.exit()
line=0
#flag checker
for i in instructions:
    if "FLAGS" in i.split() and (i.split()[0]!="mov"):
        print("Illegal Use of FLAGS register")
        sys.exit()
for i in instructions:
    if len(i.split())>2:
        if i.split()[2]=="FLAGS" and i.split()[0]!="mov":
            print("Illegal use of FLAG register")
            sys.exit()
for i in instructions:                            #printing
    s=""
    if i=="":
        continue
    elif i.split()[0]!="var":
        if type(line,i)==opcodeA:
            i=i.split()
            if(len(i)!=4):
                print("Invalid format")
                sys.exit()
            elif((i[1] not in reg.keys()) or (i[2] not in reg.keys()) or (i[3] not in reg.keys())):
                print("Invalid registers")
                sys.exit()
            else:
                s+=opcodeA[i[0]]+"00"
                s+=reg[i[1]]+reg[i[2]]+reg[i[3]]
                final.append(s)
        elif type(line,i)==opcodeB:
            i=i.split()
            if(len(i)!=3):
                print("Invalid format")
                sys.exit()
            elif(i[1] not in reg.keys()):
                print("Invalid register")
                sys.exit()
            elif(int(i[2][1:])>255 or int(i[2][1:])<0):
                print("Invalid Number")
                sys.exit()
            else:
                s+=opcodeB[i[0]]+reg[i[1]]
                s+=binary(int(i[2][1:]))
                final.append(s)
        elif type(line,i)==opcodeC:
            i=i.split()
            if(len(i)!=3):
                print("Invalid format")
                sys.exit()
            elif((i[1] not in reg.keys()) or (i[2] not in reg.keys())):
                print("Invalid Registers")
                sys.exit()
            else:
                s+=opcodeC[i[0]]+"00000"
                s+=reg[i[1]]+reg[i[2]]
                final.append(s)
        elif type(line,i)==opcodeD:
            i=i.split()
            if(len(i)!=3):
                print("Invalid Format")
                sys.exit()
            elif(i[1] not in reg.keys()):
                print("Invalid Register")
                sys.exit()
            else:
                s+=opcodeD[i[0]]+reg[i[1]]
                s+=variables[i[2]]
                final.append(s)
        elif type(line,i)==opcodeE:
            i=i.split()
            if(len(i)!=2):
                print("Invalid Format")
                sys.exit()
            else:
                s+=opcodeE[i[0]]+"000"
                if i in variables:
                    s+=variables[i[2]]
                elif i in labels:
                    s+=labels[i[2]]
                final.append(s)  
        elif type(line,i)==opcodeF:
            i=i.split()
            if(len(i)!=1):
                print("Invalid Format")
                sys.exit()
            else:
                s+=opcodeF[i[0]]+"00000000000"
                final.append(s)
        else:
            print("FATAL ERROR")
            exit(0)                                            
    line+=1
with open("output.txt","w") as o:
    for i in final:
        o.write(i)
        o.write("\n")
        
