def solve(s):
	s = list(s)
	stack = []

	while s:
		if not stack:
			stack.append(s.pop(0))
		elif stack[-1] == s[0]:
			s.pop(0)
			stack.pop()
		elif stack[-1] != s[0]:
			stack.append(s.pop(0))
	return len(stack)

t = int(input())

for i in range(1,t+1):
	s = input()

	result = solve(s)

	print(f"#{i} {result}")