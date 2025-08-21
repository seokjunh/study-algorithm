def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)

def solution(arr):
    answer = lcm(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        s = lcm(answer, arr[i])
        answer = s
    return answer