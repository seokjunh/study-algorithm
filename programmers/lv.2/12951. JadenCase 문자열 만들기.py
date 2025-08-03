def solution(s):
    words = []
    l = s.split(" ")

    for i in l:
        if i.isalpha(): 
            words.append(i[0].upper() + i[1:].lower())
        elif len(i) == 0:
            words.append(i)
        else:
            words.append(i[0].upper() + i[1:].lower)
                         
    return " ".join(words)