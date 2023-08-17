def solution(s):
    
    words = []
    for word in s.split(" "):
        answer = ''
        for idx in range(len(word)):
            if idx %2 == 0:
                answer += word[idx].upper()
            else:
                answer += word[idx].lower()
        words.append(answer)
        
    return " ".join(words)