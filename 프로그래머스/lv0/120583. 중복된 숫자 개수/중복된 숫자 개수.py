def solution(array, n):
    # answer =  filter(lambda a : a == n, array)
    answer = [a for a in array if a  == n]
    return len(answer)