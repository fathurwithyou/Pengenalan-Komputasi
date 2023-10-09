# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 9 Oktober 2023
# Deskripsi     : Program menentukan banyaknya stasiun yang dapat dikunjungi dengan uang yang sudah ditentukan

# KAMUS
# uang, n: int

# ALGORITMA
# menerima input
uang = int(input("Masukkan uang yang dibawa Tuan Leo: "))
n = int(input("Masukkan jumlah stasiun: "))

arr = [0 for i in range(n+1)]
for i in range(1, n):
    arr[i] = int(input(f"Masukkan harga stasiun ke-{i}: "))
arr[0] = int(input(f"Masukkan harga stasiun ke-{n}: "))

maxi = 0
start = 0
for i in range(1, n+1):
    j = i
    biaya = 0
    while biaya <= uang and j-i <= n:
        biaya += arr[j%n]
        j += 1
        
    if j-i-1 > maxi:
      maxi = j-i-1
      start = i
      
if maxi == 0:
  print("Tuan Leo kekurangan uang.")
else:
  print(f"Tuan Leo dapat mengunjungi {maxi} stasiun dimulai dari stasiun ke-{start}.")
