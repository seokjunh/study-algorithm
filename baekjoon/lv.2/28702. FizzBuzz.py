a = input()
b = input()
c = input()

n = 0
if a.isdigit():
	n = int(a)+3
elif b.isdigit():
	n = int(b)+2
elif c.isdigit():
	n = int(c)+1

if n % 3 == 0 and n % 5 == 0:
	print("FizzBuzz")
elif n % 3 == 0 and n % 5 != 0:
	print("Fizz")
elif n % 3 != 0 and n % 5 == 0:
	print("Buzz")
else:
	print(n)