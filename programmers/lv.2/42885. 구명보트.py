def solution(people, limit):
    answer = len(people)
    people.sort()
    
    l,r = 0,len(people)-1
    
    while l < r:
        if people[l] + people[r] <= limit:
            l += 1
            answer -= 1
        r -= 1
        
    return answer