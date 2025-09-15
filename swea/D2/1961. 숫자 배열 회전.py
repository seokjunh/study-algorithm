t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]

    print(f"#{i}")
    a, b, c = [], [], []

    for j in range(n):
        s = ""
        for k in range(n - 1, -1, -1):
            s += arr[k][j]
        a.append(s)

    for j in range(n - 1, -1, -1):
        s = ""
        for k in range(n - 1, -1, -1):
            s += arr[j][k]
        b.append(s)

    for j in range(n - 1, -1, -1):
        s = ""
        for k in range(n):
            s += arr[k][j]
        c.append(s)

    for j in range(n):
        print(a[j], b[j], c[j])
