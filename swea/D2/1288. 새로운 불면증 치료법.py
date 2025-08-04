t = int(input())

for i in range(1,t+1):
	n = int(input())

	j = 1
	s = set()
	while True:

		for k in str(n * j):
			s.add(int(k))

		if sorted(list(s)) == [0,1,2,3,4,5,6,7,8,9]:
			print(f"#{i} {n * j}")
			break

		j += 1