num = int(input())
a = list(map(int,input().split()))
for i in range(0,num):
    c = int(input())
    a.append(c)
print(a)
count = 0
for i in a:
    if(i%2==0):
        count+=1
        print(i)
if count == 0:
    print("-1")