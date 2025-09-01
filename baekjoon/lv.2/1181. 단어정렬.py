arr = set()
for _ in range(int(input())):
	arr.add(input())

l = sorted(list(arr), key=lambda x:(len(x),x))

for i in l:
	print(i)