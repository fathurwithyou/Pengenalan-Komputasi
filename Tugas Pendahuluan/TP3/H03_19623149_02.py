# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 9 Oktober 2023
# Deskripsi     : Program menentukan bilangan terbesar ke-n

# KAMUS
# m, n, i, j : int
# arr : list of int

# ALGORITMA
# menerima input
m = int(input("Masukkan banyak data: "))
n = int(input("Masukkan nilai N: "))

arr = [0 for i in range(m)]  # inisialisasi
for i in range(m):
    arr[i] = int(input(f"Masukkan data ke-{i+1}: "))

# descending bubble sort algorithm
for i in range(m):
    for j in range(i, m):
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

print(f"Nilai terbesar ke-{n} adalah {arr[n-1]}")
