def solve(n):
    ans = 1
    while n:
        ans *= n % 10
        n //= 10
    return ans


n = int(input("Masukkan sebuah bilangan: "))
cnt = 1
while n//10:
    n = solve(n)
    print(f"Setelah proses ke-{cnt}: {n}")
    cnt += 1
