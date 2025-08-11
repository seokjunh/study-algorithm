def in_order(idx):
    global value
    if idx <= n:
        in_order(idx*2)
        tree[idx] = value
        value += 1
        in_order(idx*2+1)

t = int(input())

for i in range(1, t+1):
    n = int(input())
    tree = [0] * (n+1)
    value = 1
    in_order(value)
    print(f"#{i} {tree[1]} {tree[n//2]}")