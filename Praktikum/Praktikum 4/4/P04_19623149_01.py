# NIM/Nama      : 19623149/Muhammad Fathur Rizky
# Tanggal       : 2 November 2023
# Deskripsi     : Program menentukan apakah bobot yang diberikan valid

# KAMUS
# a, b, c, soal1, soal2, soal3: float
def cekValid(a, b, c):  # fungsi mengecek apakah bobot valid
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1 and a + b + c == 1


def hitung(a, b, c, soal1, soal2, soal3):  # fungsi menghitung nilai
    return soal1*a + soal2*b + soal3*c


# ALGORITMA
# menerima input
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
soal1 = float(input("Masukkan nilai soal 1: "))
soal2 = float(input("Masukkan nilai soal 2: "))
soal3 = float(input("Masukkan nilai soal 3: "))

# proses
if cekValid(a, b, c):  # jika valid
    print(
        f"Nilai tugas praktikum adalah {hitung(a, b, c, soal1, soal2, soal3):.2f}")
else:  # jika tidak valid
    print("bobot tidak valid")

# Ide Solusi
'''
Ini merupakan soal yang hanya memerlukan pengecekan 4 kondisi saja. Jika valid maka hitung.

'''

# Sample Input
'''
0.3
0.4
0.3
100
100
0

0.3
0.4
0.2
100
100
0

0.3
1.1
-0.4
100
100
0
'''
# BISMILLAH FULL SCORE 100/100 !!!
