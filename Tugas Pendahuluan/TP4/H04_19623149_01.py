# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 23 Oktober 2023
# Deskripsi     : Program menentukan subarray maksimum 2x2 yang memiliki elemen ganjil

# KAMUS
# m, n, maxi, summ : int
# odd : bool
# arr : list of list of int

# ALGORITMA
# menerima input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
arr = [[0 for i in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j] = int(
            input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))
maxi = 0 
for i in range(m-1):
    for j in range(n-1):
        summ = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
        odd = arr[i][j]&1 or arr[i][j+1]&1 or arr[i+1][j]&1 or arr[i+1][j+1]&1 
        if odd and summ > maxi:
            maxi = summ
if maxi:
    print(
        f"Jumlah maksimum dari submatriks 2x2 yang memiliki elemen ganjil adalah {maxi}")
else:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")

'''
3
3
1
2
3
2
4
6
2
2
2

3
4
1
2
3
2
4
6
9
2
2
1
2
3

'''
