def solution(box, n):
    answer = 0
    
    s1 = box[0] // n
    s2 = box[1] // n
    s3 = box[2] // n
    
    return s1 * s2 * s3