# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 2 November 2023
# Deskripsi     : Program menentukan apakah raja aman dari serangan kuda

# KAMUS
# m, x, y: int
# arr: list of list of int
# kiri_a, kiri_b, kanan_a, kanan_b: bool
def isSafe(arr, x, y):  # fungsi untuk mengecek apakah raja aman dari serangan kuda
    kiri_a = arr[y-2][x-1] == '.' and arr[y-1][x-2] == '.'  # kiri atas
    kanan_a = arr[y-2][x+1] == '.' and arr[y-1][x+2] == '.'  # kanan atas
    kiri_b = arr[y+2][x-1] == '.' and arr[y+1][x-2] == '.'  # kiri bawah
    kanan_b = arr[y+2][x+1] == '.' and arr[y+1][x+2] == '.'  # kanan bawah

    # kiri atas dan kanan atas dan kiri bawah dan kanan bawah
    return kiri_a and kanan_a and kiri_b and kanan_b


# ALGORITMA
m = int(input("Masukkan nilai m: "))
x = y = -1  # inisialisasi koordinat raja
arr = [['.' for i in range(m+4)] for i in range(m+4)]  # inisialisasi array
for i in range(2, 2+m):
    for j in range(2, 2+m):
        arr[i][j] = input(f"Masukkan elemen matriks ke-{i-1} {j-1}: ")
        if arr[i][j] == 'R':  # jika koordinat raja ditemukan, catat
            x = j
            y = i

# Mencetak papan catur
print("Hasil papan catur")
for i in range(2, 2+m):
    for j in range(2, 2+m):
        print(arr[i][j], end=" ")  # cekta
    print()

# Proses menentukan kondisi raja
if isSafe(arr, x, y):  # jika raja aman
    print("Raja aman dari serangan kuda.", end="")
else:  # jika tidak
    print("Raja tidak aman dari serangan kuda.", end="")

# Ide Solusi
'''
Daripada kita membuat banyak if untuk mengecek apakah di dalam papan catur, lebih baik kita membuat array dengan menambah lebar petak sebanyak 2 dan panjang petak sebanyak 2.
Dengan begitu, kita bisa lebih mudah untuk membuat algo dan lebih rapih :) 
'''

# Sample Input
'''
3
K
.
K
K
R
K
.
.
.
====
4
.
.
K
.
K
.
.
.
.
R
K
.
.
.
K
.
====
5
K
.
K
.
.
.
R
.
.
.
K
.
.
K
.
.
.
K
.
.
.
.
K
.
K
'''
