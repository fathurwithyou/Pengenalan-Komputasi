# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 19 Oktober 2023
# Deskripsi     : Program menentukan berapa banyak uang yang harus dia keluarkan untuk makan di restorant

# KAMUS
# n : int
# mini, bayar : float
# harga : list of float

# ALGORITMA 
# SOLUSI NAIF
# menerima input
n = int(input("Masukkan nilai N: "))  # asumsikan N >= 3
harga = [0 for i in range(n+1)]  # deklarasi array
for i in range(n):
    harga[i] = int(input(f"Masukkan harga jam ke-{i+1}: "))
mini = harga[0] + harga[1] + harga[2] # deklarasi pembayaran terkecil
for i in range(1, n-2):
    bayar = 0
    for j in range(i, i+3): #untuk mencatat bayar setiap perulangan
        bayar += harga[j] 
    if bayar < mini:
        mini = bayar
print(f"Total harga yang harus dibayar adalah {mini}.")

# Penjelasan Solusi
'''
Kita bisa melakukan iterasi berulang untuk setiap i sebanyak 3 kali sehingga kompleksitasnya adalah
O(3*N)
'''

# Ide Solusi Lain
'''
Kita bisa membuat prefix sum dari setiap harga dan untuk menentukan berapa banyak dia harus bayar, 
kita bisa melakukan operasi bayar = arr[i] - arr[i-3] 
Time Complexity: O(N)
'''

# Kode Solusi Lain (Optimized) (Sliding Window Algorithm)
'''
n = int(input("Masukkan nilai N: "))  # asumsikan N >= 3
harga = [0 for i in range(n+1)]  # deklarasi array
for i in range(1, n+1):
    harga[i] = int(input(f"Masukkan harga jam ke-{i}: "))
    harga[i] += harga[i-1]
mini = harga[n] # deklarasi pembayaran terkecil
for i in range(3, n+1):
    if harga[i] - harga[i-3] < mini:
      mini =  harga[i] - harga[i-3]
print(f"Total harga yang harus dibayar adalah {mini}.")
'''

# Sample Input
'''
6
10000
20000
30000
40000
50000
60000

7
50000
10000
30000
20000
10000
10000
50000

4
10000
50000
50000
10000
'''

# BISMILLAH ABSOL (FULL SCOREEE)
