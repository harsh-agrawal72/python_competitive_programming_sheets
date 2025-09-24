num = int(input())
a = list(map(int,input().split()))
for i in range(1,num*2):
    c = int(input())
    a.append(c)
print(a)
percentage_list = []
attendance_list = []
for i in range(0,len(a)):
    if i%2==0:
        percentage_list.append(a[i])
    else:
        attendance_list.append(a[i])
print(percentage_list)
print(attendance_list)
count = 0
for i in range(0,len(a)/2.0):
    if(percentage_list[i]>=75 and attendance_list[i]>=80):
        count+=1
print(count)
