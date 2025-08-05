def binaryOneCheck(num):
    result = ""
    while num > 0:
        result += str(num%2)
        num //= 2
    cnt = result.count("1")
    return cnt

def solution(n):
    r = binaryOneCheck(n)
    m = n+1
    answer = 0
    
    while True:
        if r == binaryOneCheck(m):
            answer = m
            break
        m += 1
        
    return answer