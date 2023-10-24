kamus = [str(i) for i in range(10)]

plat = input()
jumlah = int(input())
banyak = int(input())

for i in range(len(plat)):
  for j in range(10):
    if kamus[j] == plat[i]:
      jumlah -= j
      banyak -= 1

if not jumlah and not banyak and plat[0] == 'D':
  print("Mobil Tuan Kil ditemukan!")
else:
  print("Bukan mobil Tuan Kil!")
      
'''
D1234ABC
10
4

D14RE
8
2

B154YUK
10
3
'''