s = input()

idx = 0
n = 0
for i in range(len(s)-1):
	if s[i] == "*":
		idx = i
	else:
		if i % 2 == 0:
			n += int(s[i])
		else:
			n += int(s[i])*3
m = int(s[-1])
for j in range(10):
	if idx % 2 == 0:
		if (n + j + m) % 10 == 0:
			print(j)
			break
	else:
		if (n + 3*j + m) % 10 == 0:
			print(j)
			break