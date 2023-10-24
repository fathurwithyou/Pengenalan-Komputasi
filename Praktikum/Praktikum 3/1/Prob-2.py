n = int(input("Panjang Papan: "))
deb = int(input("Dadu Nona Deb: "))
sal = int(input("Dadu Nona Sal: "))

deb_run = sal_run = True

arr = [0 for i in range(n+1)]
for i in range(1, n+1):
    arr[i] = int(input(f"Angka ke-{i}: "))

while deb_run or sal_run:
    if deb_run:
        deb += arr[deb]
        if deb <= 0:
            deb = 2 + deb*-1
        if deb > n:
            deb = 2*n - deb
        if arr[deb] == 0:
            deb_run = False
    if sal_run:
        sal += arr[sal]
        if sal <= 0:
            sal = 2 + sal*-1
        if sal > n:
            sal = 2*n - sal
        if arr[sal] == 0:
            sal_run = False

if deb > sal:
    print("Nona Deb Memenangkan Permainan .")
elif deb < sal:
    print("Nona Sal Memenangkan Permainan .")
else:
    print("Permainan Seri")

'''
7
2
5
0
-3
1
0
2
2
-6

6
2
4
1
0
-1
3
0
2

5
1
4
2
1
0
-2
0

'''
