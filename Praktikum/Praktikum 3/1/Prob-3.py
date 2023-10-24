n = int(input("Masukkan nilai N: "))
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input(f"Masukkan bilangan ke {i+1}: "))
for i in range(n-1, 0, -1):
    for j in range(i):
        a = arr[j]
        b = arr[j+1]
        while a > 0:
            a, b = b % a, a
        arr[j] = b
        print(arr[j], end=" ")
    print()
print(f"Nilai FPB berantainya adalah {arr[0]}.")

'''
5
8
6
12
5
10

3
4
12
24

4
20
40
12
20

'''
