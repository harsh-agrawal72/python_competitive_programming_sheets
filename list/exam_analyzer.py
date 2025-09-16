num = int(input())
a = list(map(int,input().split()))
for i in range(0,num):
    c = int(input())
    a.append(c)
print(a)
pass_count = 0
fail_count = 0
for i in a:
    if i>=35:
        pass_count+=1
    else:
        fail_count+=1
print(pass_count)
print(fail_count)