# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 23 Oktober 2023
# Deskripsi     : Program menentukan banyaknya kapal musuh pada peta

# KAMUS
# n, m, ans : int
# arr : list of list of char

# ALGORITMA
# menerima input
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
arr = [0 for i in range(n)] # deklarasi array
ans = 0 # deklarasi jawaban

# fungsi yang digunakan untuk mengubah 1 menjadi 0
def dfs(x, y):
    i, j = x, y+1
    if 0 <= i < n and 0 <= j < m:
        while arr[i][j] == '1':
            arr[i][j] = '0'
            if 0 < j < m-1:
                j += 1
    i, j = x+1, y
    if 0 <= i < n and 0 <= j < m:
        while arr[i][j] == '1':
            arr[i][j] = '0'
            if 0 < i < n-1:
                i += 1


print("Masukkan peta:")
# menerima input
for i in range(n):
    arr[i] = list(input())
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1': # jika ada 1
            ans += 1
            arr[i][j] = '0'
            dfs(i, j)
if ans: #jika jawaban tidak 0
    print(f"Terdapat {ans} kapal musuh pada peta")
else:
    print("Tidak terdapat kapal musuh pada peta")
'''
3
3
000
000
000

4
5
11110
00000
11100
00000

5
6
111100
000001
001000
001001
110001

'''
