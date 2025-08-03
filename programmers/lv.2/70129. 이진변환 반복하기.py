def solution(s):
    answer = [0,0]
    
    while True:
        
        if s == "1":
            break
            
        zero = s.count("0")
        one = len(s) - zero
        
        result = ""
        while one >= 1:
            result += str(one % 2)
            one = one // 2
            
        s = result[::-1]
        
        answer[0] += 1
        answer[1] += zero
    
    return answer
    
            
            
        
        