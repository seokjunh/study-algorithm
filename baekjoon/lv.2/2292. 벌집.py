n = int(input())

start = 1
i = 0
while True:
	start += (6 * i)
	i += 1

	if start >= n:
		print(i)
		break