def base64Decoder(s):
	bi = ""
	for i in s:
		c = table.index(i)

		r = ""

		while c > 0:
			r += str(c % 2)
			c = c //2

		if len(r) < 6:
			l = 6 - len(r)
			r += l*"0"

		bi += r[::-1]
		
	result = ""
	for i in range(0,len(bi),8):
		g = 0
		for j in range(len(bi[i:i+8][::-1])):
			if bi[i:i+8][::-1][j] == "1":
				g += 2**j
		result += chr(g)

	return result

n = int(input())

table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for i in range(n):
	result = base64Decoder(input())
	print(f"#{i+1} {result}")