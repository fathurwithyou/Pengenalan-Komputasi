n = int(input())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
print(end="0-")
for i in range(n):
    j = i-1
    run = True
    while j >= 0 and arr[j] <= arr[i]:
        j -= 1
    print(i-j-1, end="")
    if i < n-1:
        print(end='-')

'''
5
12
12
24
15
18

7
120
40
30
65
50
250
50

8
17
25
40
13
45
10
48
15

'''
