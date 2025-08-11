def isPalindrome(s):
	if s == s[::-1]:
		return True
	return False

t = int(input())

for i in range(1,t+1):
	s = input().strip()
	if isPalindrome(s):
		print(f"#{i} 1")
	else:
		print(f"#{i} 0")