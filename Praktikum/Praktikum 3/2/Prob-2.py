n = int(input("Masukkan banyak bangunan: "))
arr = [0 for i in range(n+2)]
for i in range(1, n+1):
    arr[i] = int(input(f"Masukkan tinggi bangunan ke-{i}: "))
t = int(input("Masukkan nomor bangunan yang akan disewa: "))
cocok = True
for i in range(1, arr[t]//2+1):
    if t-i >= 0:
        if arr[t-i] > arr[t]:
            cocok = False
            i = n
    if t+i <= n:
        if arr[t+i] > arr[t]:
            cocok = False

if cocok:
    print(f"Bangunan ke-{t} cocok untuk disewa oleh Nona Sal")
else:
    print(f"Bangunan ke-{t} tidak cocok untuk disewa oleh Nona Sal")

'''
5
1
3
1
3
4
2

3
2
7
4
1


9
11
3
2
4
6
9
4
2
1
6

'''
