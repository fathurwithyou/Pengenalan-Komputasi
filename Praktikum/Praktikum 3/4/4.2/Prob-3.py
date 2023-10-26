s = input()
l = 0
for i in range(len(s)):
    if s[i] == 'ˆ':
        for j in range(l, i-1, 2):
            print(f"{s[j+1]}{s[j]}", end="")
        if (i-l) & 1:
            print(s[i-1], end="")
        print(end=" ")
        l = i + 1
    if s[i] == '*':
        for j in range(i-1, l-1, -1):
            print(s[j], end="")
        print(end=" ")
        l = i + 1

# Sample Input
'''
iniˆadalah*contoh*kataˆrahasia*

kota pengkom*

kota pengkomˆ
'''
