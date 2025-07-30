t = int(input())

for i in range(t):
    n = int(input())

    answer = [0,0,0,0,0]

    while n > 1:
        if n % 2 == 0:
            answer[0] += 1
            n //= 2
        elif n % 3 == 0:
            answer[1] += 1
            n //= 3
        elif n % 5 == 0:
            answer[2] += 1
            n //= 5
        elif n % 7 == 0:
            answer[3] += 1
            n //= 7
        elif n % 11 == 0:
            answer[4] += 1
            n //= 11
            
    print(f"#{i+1}", end=" ")
    print(*answer)