# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 23 Oktober 2023
# Deskripsi     : Program menentukan banyaknya kapal musuh pada peta

# KAMUS
# n, m, ans : int
# dp : list of list of char

# ALGORITMA
# menerima input
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
dp = [['0' for i in range(m+1)] for i in range(n+1)]
cnt = 0
print("Masukkan peta:")
for i in range(1, n+1):
    s = input()
    for j in range(1, m+1):
        dp[i][j] = s[j-1]
        cnt += dp[i-1][j] == '0' and dp[i][j-1] == '0' and dp[i][j] == '1'
if cnt:
    print(f"Terdapat {cnt} kapal musuh pada peta")
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
