n,m = map(int, input().split())

card = list(map(int, input().split()))

card.sort()

answer = 0
for i in range(len(card)):
	for j in range(i+1, len(card)):
		for k in range(j+1, len(card)):
			if card[i]+card[j]+card[k] > m:
				break
			if card[i]+card[j]+card[k] <= m:
				answer = max(answer, card[i]+card[j]+card[k])
print(answer)