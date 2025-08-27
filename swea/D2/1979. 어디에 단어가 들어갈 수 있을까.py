t = int(input())

for idx in range(1, t+1):
	n,k = map(int, input().split())

	arr = [list(map(int, input().split())) for _ in range(n)]

	answer = 0

	for i in range(n):
		s = 0
		# 가로
		for j in range(n):
			if arr[i][j] == 1:
				s += 1
			if arr[i][j] == 0 or j == n - 1:
				if s == k:
					answer += 1
				s = 0

		# 세로
		for j in range(n):
			if arr[j][i] == 1:
				s += 1
			if arr[j][i] == 0 or j == n - 1:
				if s == k:
					answer += 1
				s = 0
	print(f"#{idx} {answer}")