def command(str,pbk):
    if(str[0] == "add"):
        for i in range(len(pbk)):
            if(pbk[i][0] == int(str[1])):
                pbk[i][1] = str[2]
                return
        pbk.append([int(str[1]),str[2]])
    elif(str[0] == "find"):
        for i in range(len(pbk)):
            if(pbk[i][0] == int(str[1])):
                print(pbk[i][1])
                return
        print("not found")
    elif(str[0] == "del"):
        for i in range(len(pbk)):
            if(pbk[i][0] == int(str[1])):
                pbk.pop(i)
                return
    return



t = int(input())
pbk = []
for i in range(t):
    command(input().split(' '),pbk)

