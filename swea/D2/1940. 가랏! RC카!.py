t = int(input())

for i in range(1, t + 1):
    n = int(input())
    d, v = 0, 0
    for j in range(n):
        arr = list(map(int, input().split()))

        if arr[0] == 1:
            v += arr[1]
        elif arr[0] == 2:
            v -= arr[1]
            if v < 0:
                v = 0
        d += v
    print(f"#{i} {d}")
