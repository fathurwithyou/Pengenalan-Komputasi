dp = [0 for i in range(101)]
n = int(input("Masukkan banyak rumah yang dihuni: "))
for i in range(1, n+1):
    dp[int(input(f"Masukkan nomor rumah ke-{i}: "))] = 1
maxi = dp[1]
for i in range(2, 101):
    if dp[i] and dp[i-1]:
        dp[i] += dp[i-1]
    elif dp[i] and dp[i-2]:
        dp[i] += dp[i-2]
    if dp[i] > maxi:
        maxi = dp[i]
print(
    f"Kemungkinan terburuk banyak rumah yang terinfeksi adalah {maxi} rumah.")

'''
2
1
4

3
1
2
4

5
1
2
5
7
9

5
1
2
3
4
5

'''
