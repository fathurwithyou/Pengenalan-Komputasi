# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 19 Oktober 2023
# Deskripsi     : Program  menentukan jumlah potongan list yang jika seluruh elemen penyusun potongannya dijumlahkan akan menghasilkan bilangan prima.

# KAMUS
# n, sum, ans : int
# is_prime : bool
# arr : list of int

# ALGORITMA
n = int(input("Masukkan nilai N: "))  # menerima input N
arr = [0 for i in range(n)]  # inisialisasi array
for i in range(n):
    # menerima input elemen
    arr[i] = int(input(f"Masukkan bilangan ke {i+1}: "))
ans = 0  # deklarasi jawaban
for i in range(n):
    summ = 0  # inisialisasi summ
    for j in range(i, n):
        is_prime = True # anggapan awal
        summ += arr[j] # menambahkan summ setiap subarray
        if summ <= 1:  # bilangan <= 1 pasti bukan prima
            is_prime = False
        for k in range(2, summ//2+1):  # primality test
            if summ % k == 0:
                is_prime = False
                k = summ  # manual break
        if is_prime:  # jika prima, maka tambahkan
            ans += 1
if ans > 0:  # jika ada potongan list
    print(f"Terdapat {ans} potongan list yang jumlahnya prima.")
else:  # jika tidak ada
    print("Tidak ada potongan list yang jumlahnya prima.")
    
# Penjelasan Solusi
'''
Kita bisa melakukan pengecekan berulang kali untuk menentukan apakah 
jumlah dari bilangannya adalah prima.
'''

# Sample Input
'''
6
2
5
17
8
3
1

4
1
1
1
1

5
4
8
12
16
20
'''

# BISMILLAH ABSOL (FULL SCOREEE)
