from collections import Counter

t = int(input())

for j in range(t):
    str1 = input()
    str2 = input()

    counter = Counter(str2)

    answer = 0
    for i in str1:
        if i in counter:
            answer = max(answer, counter[i])
    
    print(f"#{j+1} {answer}")