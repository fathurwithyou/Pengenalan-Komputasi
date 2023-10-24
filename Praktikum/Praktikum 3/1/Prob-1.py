n = int(input("Masukkan banyak robot: "))
s = input("Masukkan konfigurasi robot: ")
ans = 0
for i in range(n//2):
    ans += int(s[i])
    ans -= int(s[n-i-1])
if ans > 0:
    print("Sisi kiri menang!")
elif ans < 0:
    print("Sisi kanan menang!")
else:
    print("Berakhir seri!")

'''
4
1234

6
165403

8
11112200
'''