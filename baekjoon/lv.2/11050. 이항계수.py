def factorial(s):
	if s <= 1:
		return 1
	return s * factorial(s-1)

n,k = map(int, input().split())

answer = factorial(n) // (factorial(n-k) * factorial(k))

print(answer)