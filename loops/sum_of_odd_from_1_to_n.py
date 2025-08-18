num = int(input("enter any number: "))
count=1
sum = 0
while(count<=num):
    if(count%2!=0):
        sum+=count
    count+=1
print("sum from 1 to",num,"is :",sum)