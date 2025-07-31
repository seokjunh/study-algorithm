n = int(input())
s = list(map(int, input().split()))
t,p = map(int, input().split())

c = 0
for i in s:
	if i % t == 0:
		c += i // t
	else:
		c += i // t + 1

print(c)
print(n // p, n % p)