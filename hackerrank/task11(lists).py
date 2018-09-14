N = int(raw_input())
li = []
for i in range(N):
    string = raw_input().split()
    command = string[0]
    num = string[1:]
    if command!='print':
        com = ','
        command2 = command+'('+com.join(num)+')'
        eval('li.'+command2)
    else:
        print(li)
