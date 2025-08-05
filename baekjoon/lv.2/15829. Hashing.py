l = int(input())
s = input()

r,m = 31,1234567891

total = 0
for i in range(len(s)):
	o = ord(s[i]) - 96
	total += o* (r**i)

result = total%m

print(result)