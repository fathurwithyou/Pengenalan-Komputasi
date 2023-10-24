# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 23 Oktober 2023
# Deskripsi     : Program menentukan jumlah bakteri tersebut ketika ditinggal Nona Deb selama K detik.

# KAMUS
# n, k : int
# dp : list of int
# ALGORITMA
# fungsi dengan menggunakan DP optimization
def solve(n, k):
    dp = [0 for i in range(k+1)]
    dp[0] = n
    dp[1] = n*2+dp[0]
    for i in range(2, k+1):
        dp[i] = (dp[i-1]-dp[i-2])*2+dp[i-1]
    return dp[k] # mengeluarkan nilai dp[k]

# menerima input
n = int(input("Masukkan N: "))
k = int(input("Masukkan K: "))
#cetak keluaran
print(f"Terdapat {solve(n, k)} Bakteri Pengkombacter.")
