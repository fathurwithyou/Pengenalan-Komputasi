n = int(input("Masukkan nilai n: "))
print("Masukkan elemen matriks:")
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
print("Hasil matriks akhir:")
for i in range(2*n):
    for j in range(2*n):
        print(arr[i//2][j//2], end=" ")
    print()
'''
3
1 2 3
4 5 6
7 8 9

4
1 0 0 1
0 1 1 0
0 1 1 0
1 0 0 1

'''
