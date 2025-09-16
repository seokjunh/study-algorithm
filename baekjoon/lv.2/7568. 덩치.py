import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

answer = [1] * n

for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            answer[i] += 1
print(*answer)
