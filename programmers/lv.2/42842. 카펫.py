def solution(brown, yellow):
    answer = [0,0]
    for i in range(1, int(yellow**0.5)+1):
        r = i
        c = yellow // i
        
        if ((r+2) + c) * 2 == brown:
            answer[0] = c+2
            answer[1] = r+2
    return answer