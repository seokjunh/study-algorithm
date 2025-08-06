t = int(input())

for i in range(1,t+1):
	p,q,r,s,w = map(int,input().split())

	A,B = 0,0

	A = w * p

	B = q if w <= r else q + (w-r)*s

	print(f"#{i} {min(A,B)}")