from collections import Counter


def solution(want, number, discount):
    d = {}
    for i in range(len(want)):
        d[want[i]] = number[i]

    n = len(discount)

    answer = 0

    for i in range(n - 10 + 1):
        t = discount[i : i + 10]

        if len(Counter(d) - Counter(t)) == 0:
            answer += 1

    return answer
