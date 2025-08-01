n = int(input())
s = list(map(int, input().split()))

for i in s:
	if i == 1:
		n -= 1
	for j in range(2, int(i**0.5)+1):
		if i % j == 0:
			n -= 1
			break
print(n)