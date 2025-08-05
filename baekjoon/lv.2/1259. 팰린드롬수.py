def isPalindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	return False

while True:
	n = int(input())

	if n == 0:
		break

	if isPalindrome(n):
		print("yes")
	else:
		print("no")