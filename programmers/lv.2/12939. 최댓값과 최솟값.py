def solution(s):
    l = sorted(list(map(int, s.split(" "))))
    return str(l[0]) +" "+ str(l[-1])