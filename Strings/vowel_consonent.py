a = int(input())
for i in range(a):
    s = input().strip().lower()
    count_vowel = 0
    count_consonant = 0
    for j in s:
        if j in 'aeiou':
            count_vowel += 1
        else:
            count_consonant += 1
    print(count_vowel, count_consonant)
