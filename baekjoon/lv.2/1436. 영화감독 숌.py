n = int(input())

answer = 666

i = 1
while True:

	if i == n:
		print(answer)
		break

	answer += 1
	
	if "666" in str(answer):
		i += 1