t = int(input())

for i in range(t):
    n,m = map(int, input().split())

    l = list(map(int, input().split()))

    for _ in range(m):
        l.append(l.pop(0))
    print("#"+str(i+1)+" "+str(l[0]))