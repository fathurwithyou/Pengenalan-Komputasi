# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 2 November 2023
# Deskripsi     : Program membuat matriks hasil dari penjumlahan elemen-elemen di sekitar matriks awal (di atas, di bawah, di kiri, dan di kanan).

# KAMUS
# m, n: int
# arr, dp: list of list of int
def nearSum(arr, i, j):
    return arr[i][j-1] + arr[i][j+1] + arr[i-1][j] + arr[i+1][j]

# ALGORITMA
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
# inisialisasi dua array
arr = [[0 for i in range(n+2)] for i in range(m+2)]
dp = [[0 for i in range(n)] for i in range(m)]
for i in range(1, m+1):
    for j in range(1, n+1):
        arr[i][j] = int(
            input(f"Masukkan elemen matriks baris {i} kolom {j}: "))

# Proses memasukkan hasil ke dp array
for i in range(1, m+1):
    for j in range(1, n+1):
        print(nearSum(arr, i, j), end=" ")
    print()
# Ide Solusi
'''
Daripada kita membuat banyak if untuk mengecek agar tidak out of range, lebih baik kita membuat array dengan menambah lebar sebanyak 1 dan panjang sebanyak 1.
Dengan begitu, kita bisa lebih mudah untuk membuat algo dan lebih rapih :) 
'''

# Sample Input
'''
3
3
2
3
4
2
2
3
2
9
7
========
5
5
2
4
5
6
1
4
8
6
2
0
3
1
4
6
7
4
2
4
6
9
0
2
1
2
4
======
3
4
1
2
3
4
5
6
7
8
8
10
1
3




'''
