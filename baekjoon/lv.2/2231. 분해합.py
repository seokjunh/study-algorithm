n = int(input())

for i in range(1,n+1):
	s = str(i)
	result = i

	for j in range(len(s)):
		result += int(s[j])

	if n == result:
		print(i)
		break
else:
	print(0)