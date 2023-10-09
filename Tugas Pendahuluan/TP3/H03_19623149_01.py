# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 9 Oktober 2023
# Deskripsi     : Program menentukan siapa saja nomor-nomor perwakilan yang tidak mendatangi acara

# KAMUS
# n, m : int
# arr : list

# ALGORITMA
# menerima input
n = int(input("Masukkan nilai N: "))
m = int(input("Masukkan nilai M: "))

# inisialisasi sebuah array of frequent
arr = [0 for i in range(n+1)]

# menambahkan frekuensi kehadiran
for i in range(m):
    arr[int(input(f"Masukkan data ke-{i+1}: "))] += 1
    
print("Nomor perwakilan yang tidak datang: ", end="")

# mencetak yang tidak hadir
for i in range(1, n+1):
    if arr[i] == 0:
        print(i, end=" ")
