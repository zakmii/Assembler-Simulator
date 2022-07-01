from os import system
system("cls")
def binary(x):
    s=bin(x)
    s=s[2::]
    while(len(s)<8):
        s+="0"
    return s    
opcodeA={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"}
opcodeB={"rs":"11000","ls":"11001","mov":"10010"}
opcodeC={"mov":"10011","div":"10111","not":"11101","cmp":"11110"}
opcodeD={"ld":"10100","st":"10101"}
opcodeE={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}
opcodeF={"hlt":"01010"}
reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
#focused your attention kya hota hai bhai
#me toh tab mute karke beittha hoon
print(binary(100))