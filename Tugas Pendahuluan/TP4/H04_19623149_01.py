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
# 2-dimensional array initialization
arr = [[0 for i in range(n)] for i in range(m)]
print(arr)
for i in range(m):
    for j in range(n):
        # menerima input
        arr[i][j] = int(
            input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

maxi = 0  # inisialisasi nilai maks
for i in range(m-1):
    for j in range(n-1):
        # deklarasi setiap perulangan
        summ = 0
        odd = False
        # mencari sum of 2x2 subarray
        for k in range(i, i+2):
            for l in range(j, j+2):
                summ += arr[k][l]
                if arr[k][l] & 1:  # jika subarray terdapat elemen ganjil
                    odd = True
        # jika subarray terdapat elemen ganjil dan sum of 2x2 subarray lebih besar dari yang sekarang
        if odd and summ > maxi:
            maxi = summ
# jika maxi berubah
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
