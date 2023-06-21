def solution(cipher, code):
    answer = ''
    for idx in range(1, len(cipher) // code + 1):
        answer +=cipher[idx * code -1]
        
    return answer