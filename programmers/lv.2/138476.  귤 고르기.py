def solution(k, tangerine):
    answer = 0
    
    cnt = {}
    for i in tangerine:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    
    s = sorted(cnt.values(),reverse=True)
    
    t = 0
    for i in s:
        t += i
        answer += 1
        if t >= k:
            break
    return answer