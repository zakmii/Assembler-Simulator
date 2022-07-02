f=open("","r")
list_temp=f.readlines()
list_full=[]
for i in range(len(list_temp)):
    if(len(list_temp[i].strip())!=0):
        list_full.append(list_temp[i].strip())

dict_var={}
dict_labels={}
list_instr=[]
counter=0
for i in range(len(list_full)):
    temp=list_full[i].split()
    if temp[0]=="var":
        dict_var[temp[1]]=(i,0)
    elif temp[0][-1]==":":
        dict_labels[temp[0][:-1]]=counter
        temp.pop(0)
        list_instr.append(temp)
        counter+=1
    else:
        list_instr.append(temp)
        counter+=1

strt_addr=len(list_instr)
for i in dict_var:
    dict_var[i][0]+=strt_addr



def create_isa():
    for i in range(len(list_instr)):
        if list_instr[i][0]==



