# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 19 Oktober 2023
# Deskripsi     : Program menentukan kebenaran tulisan Komi

# KAMUS
# n_asli, n_tulis, idx : int
# asli, tulis : string
# same : bool

# ALGORITMA

# menerima input
n_asli = int(input("Masukkan panjang kata asli: "))
asli = input("Masukkan kata asli: ")
n_tulis = int(input("Masukkan panjang kata yang ditulis: "))
tulis = input("Masukkan kata yang ditulis: ")

# inisialisasi
same = True
idx = 0

if n_asli*(n_asli+1)//2 != n_tulis:  # mengecek apakah panjang kata tulis memenuhi
    same = False
if same:
    for i in range(1, n_asli+1):
        for j in range(i):
            if asli[j] != tulis[idx]:  # jika berbeda
                same = False
                j = i # manual break
            idx += 1
print()
if same:
    print("Tulisan Komi sudah benar.")
else:
    print("Tulisan Komi masih salah.")

# Penjelasan Solusi
'''
Daripada kita membuat string baru dan menambahkan katanya setiap perulangan,
lebih baik kita membuat perulangan untuk cek setiap kata pada perulangannya sama atau tidak.

Bagaimana mengeceknya? Contoh, kata sapi
Setiap perulangan, akan menghasilkan 
s
sa
sap
sapi

Dari sini kita bisa melakukan perulangan, seperti ini.
idx_tulis = 0
for i <- 1, N do
  for j <- 0, i-1 do
    if asli[j] != tulis[idx] then
      same <- False
    end if
    idx <- idx + 1
  end for
end for
'''

# Sample Input
'''
5
gelas
15
ggegelgelagelas

4
sapi
10
ssasipsapi

3
air
6
aaiair
'''

# BISMILLAH ABSOL (FULL SCOREEE)
