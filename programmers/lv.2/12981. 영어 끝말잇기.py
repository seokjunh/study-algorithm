def solution(n, words):
    stack = []
    for i in range(len(words)):
        if not stack:
            stack.append(words[i])
        else:
            if stack[-1][-1] != words[i][0] or words[i] in stack:
                return [i % n + 1, i // n + 1]
            else:
                stack.append(words[i])

    return [0, 0]
