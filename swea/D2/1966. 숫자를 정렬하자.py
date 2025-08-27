t = int(input())

for i in range(1,t+1):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	print(f"#{i}",end=" ")
	print(*arr)