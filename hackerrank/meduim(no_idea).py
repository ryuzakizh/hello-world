n = input()
arrai = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
sum = 0
for r in arrai:
    if r in A:
        sum+=1
    elif r in B:
        sum-=1
print(sum)
