def solve(a,b):
    answer = 0

    if len(a) > len(b):
        a,b = b,a

    for i in range(len(b) - len(a) + 1):
        
        total = 0
        for j in range(len(a)):
            total += a[j] * b[i+j]
        answer = max(answer, total)

    return answer


t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = solve(a,b)

    print(f"#{i} {result}")