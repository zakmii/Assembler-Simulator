import sys
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
line_no = 1
instruction_line_no = []
#f=open("input.txt","r")
#instructions=f.read()
instructions=sys.stdin.read()
           #reading assembly code from input file to count lines
instructions=instructions.split("\n")
for line in instructions:                   #reading file line by line
    if len(line.strip())!=0:
        if line.split()[0]=="var":
            instruction_line_no.append([line_no, line])
            line_no += 1
            continue
        else:
            instruction_line_no.append([line_no, line])
            line_no += 1
    elif len(line)==0:
        instruction_line_no.append([line_no, line])
        line_no += 1
        continue
    else:
        instruction_line_no.append([line_no, line])
        line_no += 1
        pc+=1
# print(instructions)
# print(instruction_line_no)
        
def type(pc,l):
    if l.split()[0] in opcodeA.keys():
        return opcodeA
    elif l.split()[0].strip() in opcodeB.keys():
        if l.split()[0].strip()=="mov" and len(l.split())!=3:
            print("Line No:" +str(iln[0])+" Instruction is Invalid")
            sys.exit()
        elif l.split()[2][0]=="$":
            return opcodeB
    elif l.split()[0].strip() in opcodeC.keys():
        return opcodeC
    elif l.split()[0] in opcodeD.keys():
        return opcodeD
    elif l.split()[0] in opcodeE.keys():
        return opcodeE
    elif l.split()[0] in opcodeF.keys():
        return opcodeF
    else:
        print("Line No:" +str(iln[0])+" Instruction is Invalid")
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
for iln in instruction_line_no:
    no, i = iln[0], iln[1]
    if len(i.split())==0:
        continue
    if ":" in i.split()[0]:
        if i.split()[0][:-1] in labels.keys():
            print("Line no: "+str(iln[0])+" label declared multiple times")
            sys.exit()
        if (i.split()[0][:-1] in opcodeA.keys()) or (i.split()[0][:-1] in opcodeB.keys()) or (i.split()[0][:-1] in opcodeC.keys()) or (i.split()[0][:-1] in opcodeD.keys()) or (i.split()[0][:-1] in opcodeE.keys()) or (i.split()[0][:-1] in opcodeF.keys()):
            print(f"Line No:{no} Instruction cannot be used as Label")
            sys.exit()
        elif ((len(i.split())>=2) and (":" in i.split()[1])):
            print(f"Line No:{no} General Syntax Error")
            sys.exit()
        labels[i.split()[0][:-1]]=binary(lines)
        lines+=1
    elif i.split()[0]!="var" and i.split()[0]!="":
        lines+=1
    #variables
for iln in instruction_line_no:
    no, i = iln[0], iln[1]
    if len(i.split())==0:
        continue
    if i.split()[0]=="var":
        if len(i.split())!=2:
            print(f"Line no: "+str(iln[0])+" No Variable Name given")    
            sys.exit()
        if i.split()[1].isalnum()==False:
            print("Line no: "+str(iln[0])+" variable names can only be alphanumeric")
            sys.exit()
        if (i.split()[1]=="var") or (i.split()[1] in labels.keys()) or (i.split()[1] in opcodeA.keys()) or (i.split()[1] in opcodeB.keys()) or (i.split()[1] in opcodeC.keys()) or (i.split()[1] in opcodeD.keys()) or (i.split()[1] in opcodeE.keys()) or (i.split()[1] in opcodeF.keys()):
            print("Invalid Variable Name")
            sys.exit()
        if i.split()[1] in variables.keys():
            print("Line no: "+str(iln[0])+"  Variable Declared multiple times")
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
    if i.strip()!="":
        temp.append(i)
if "hlt" not in temp[-1]:
        print("Halt not used at the end")
        sys.exit()
for i in range(0,len(temp)-1):
    tempo=temp[i]
    if ":" in tempo:
        tempo=tempo[(tempo.find(":")+2):]
        if tempo!="":
            if tempo.split()[0]=="hlt":
                print("Halt used before last line")
                sys.exit()
    if tempo!="":
            if tempo.split()[0]=="hlt":
                print("Halt used before last line")
                sys.exit()

#flag checker
for iln in instruction_line_no:
    no, i = iln[0], iln[1]
    if len(i.split())>2:
        if i.split()[2]=="FLAGS" and i.split()[0]=="mov":
            print(f"Line no:{no} Illegal use of FLAG register")
            sys.exit()

line=0
for iln in instruction_line_no: #printing
    no, i = iln[0], iln[1]                            
    s=""
    if i.strip()=="":
        continue
    elif i.split()[0]!="var":
        if ":" in i:
            u=0
            while(":" in i):
                x=i.index(":")+1
                i=i[x::]
            if u>1:
                print(f"Line no. {line}: More than 1 label in single line")
            j=i
            if j.strip()=="":
                continue
        if type(line,i)==opcodeA:
            i=i.split()
            if(len(i)!=4):
                print(f"Line no {no}: Invalid format")
                sys.exit()
            elif((i[1] not in reg.keys()) or (i[2] not in reg.keys()) or (i[3] not in reg.keys())):
                print(f"Line no {no}: Invalid registers")
                sys.exit()
            else:
                s+=opcodeA[i[0]]+"00"
                s+=reg[i[1]]+reg[i[2]]+reg[i[3]]
                final.append(s)
        elif type(line,i)==opcodeB:
            i=i.split()
            if(len(i)!=3):
                print(f"Line no {no}: Invalid format")
                sys.exit()
            elif(i[1] not in reg.keys()):
                print(f"Line no {no}: Invalid register")
                sys.exit()
            elif(not i[2][1:].isnumeric() or float(i[2][1:])>255 or float(i[2][1:])<0):
                print(f"Line no {no}: Invalid Number")
                sys.exit()
            else:
                s+=opcodeB[i[0]]+reg[i[1]]
                s+=binary(int(i[2][1:]))
                final.append(s)
        elif type(line,i)==opcodeC:
            i=i.split()
            if(len(i)!=3):
                print(f"Line no {no}: Invalid format")
                sys.exit()
            elif((i[1] not in reg.keys()) or (i[2] not in reg.keys())):
                print(f"Line no {no}: Invalid Registers")
                sys.exit()
            else:
                s+=opcodeC[i[0]]+"00000"
                s+=reg[i[1]]+reg[i[2]]
                final.append(s)
        elif type(line,i)==opcodeD:
            i=i.split()
            if(len(i)!=3):
                print(f"Line no {no}: Invalid Format")
                sys.exit()
            elif(i[1] not in reg.keys()):
                print(f"Line no {no}: Invalid Register")
                sys.exit()
            elif(i[2] not in variables.keys()):
                print(f"Line no {no}: Undeclared Variable")
                exit(0)
            else:
                s+=opcodeD[i[0]]+reg[i[1]]
                s+=variables[i[2]]
                final.append(s)
        elif type(line,i)==opcodeE:
            i=i.split()
            if(len(i)!=2):
                print(f"Line no {no}: Invalid Format")
                sys.exit()
            elif(i[1] not in labels.keys()):
                print(f"Line no {no}: Undeclared Labels")
                exit(0)    
            else:
                s+=opcodeE[i[0]]+"000"
                if i[1] in variables.keys():
                    s+=variables[i[1]]
                elif i[1] in labels.keys():
                    s+=labels[i[1]]
                final.append(s)  
        elif type(line,i)==opcodeF:
            i=i.split()
            if(len(i)!=1):
                print(f"Line no {no}: Invalid Format")
                sys.exit()
            else:
                s+=opcodeF[i[0]]+"00000000000"
                final.append(s)
        else:
            print(f"Line no {no}: FATAL ERROR")
            exit(0)                                            
    line+=1

for i in final:
    print(i)
# with open("output.txt","w") as o:
#     for i in final:
#         o.write(i)
#         o.write("\n")

#print(labels)
#print(variables)
