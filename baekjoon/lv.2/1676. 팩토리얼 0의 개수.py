n = int(input())


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


result = factorial(n)
cnt = 0
for i in str(result)[::-1]:
    if i != "0":
        print(cnt)
        break
    else:
        cnt += 1
