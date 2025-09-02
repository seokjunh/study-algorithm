def solution(elements):
    answer = set()
    n = len(elements)
    elements *= 2

    for i in range(1, n + 1):
        s = sum(elements[:i])
        answer.add(s)
        for j in range(1, n):
            s = s - elements[j - 1] + elements[j + i - 1]
            answer.add(s)

    return len(answer)
