num = int(input())
for i in range(num):
    s = input().strip().lower()
    if s == s[::-1]:
        print(1)
    else:
        print(0)