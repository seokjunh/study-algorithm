t = int(input())

for i in range(1, t+1):
	s = input()

	d = {}

	for j in s:
		if j in d:
			d[j] += 1
		else:
			d[j] = 1

	m = min(d.values())

	answer = 0
	for k in d:
		if d[k] == m:
			answer += 1
		elif d[k] >= m:
			answer += d[k] // m
	print(f"#{i} {answer}")