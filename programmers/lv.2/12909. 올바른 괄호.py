def solution(s):
    stack = []
    
    if s[0] == ")":
        return False

    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == "(" and s[i] == ")":
                stack.pop()
            else:
                stack.append(s[i])
    if not stack:
        return True
    return False

