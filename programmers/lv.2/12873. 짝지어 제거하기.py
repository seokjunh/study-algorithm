from collections import deque

def isClear(i):
    i = deque(i)
    stack = [] 
    
    while i:
        if not stack:
            stack.append(i.popleft())
        elif stack[-1] == i[0]:
            stack.pop()
            i.popleft()
        elif stack[-1] != i[0]:
            stack.append(i.popleft())
        
    if not stack:
        return True
    return False

def solution(s):
    if isClear(s):
        return 1
    return 0