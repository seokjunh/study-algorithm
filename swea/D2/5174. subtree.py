def bfs(k):
	answer = 1

	for i in tree[k]:
		answer += bfs(i)
	return answer

t = int(input())

for i in range(1,t+1):
	e,n = map(int, input().split())

	l = list(map(int, input().split()))

	tree = [[] for _ in range(e+2)]

	for j in range(0,len(l),2):
		tree[l[j]].append(l[j+1])
	
	result = bfs(n)

	print(f"#{i} {result}")