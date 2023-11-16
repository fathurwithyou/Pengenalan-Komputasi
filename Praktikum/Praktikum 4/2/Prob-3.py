def baris(arr, p):
    for i in range(n):
        for j in range(i+1, n):
            if arr[p][j] < arr[p][i]:
                arr[p][j], arr[p][i] = arr[p][i], arr[p][j]
    return arr


def kolom(arr, p):
    for i in range(m):
        for j in range(i+1, m):
            if arr[j][p] < arr[i][p]:
                arr[j][p], arr[i][p] = arr[i][p], arr[j][p]
    return arr


m = int(input("Masukkan nilai M: "))
n = int(input("Masukkan nilai N: "))
arr = [[0 for i in range(m)] for i in range(n)]
for i in range(m):
    arr[i] = list(map(int, input().split()))

chg = int(input("Banyak Perubahan: "))
for i in range(chg):
    axis = input(f"Perubahan Ke-{i+1}: ")
    if axis == "baris":
        p = int(input("Masukkan baris yang diubah: "))
        arr = baris(arr, p-1)
    if axis == "kolom":
        p = int(input("Masukkan kolom yang diubah: "))
        arr = kolom(arr, p-1)
for i in range(m):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
'''
3
5
20 19 18 17 16
15 14 13 12 11
10 21 29 28 27
2
baris
2
kolom
2

4
5
8 1 4 2 6
5 3 1 9 7
4 2 5 2 4
8 6 2 4 1
3
baris
3 
baris
2
kolom
1

'''
