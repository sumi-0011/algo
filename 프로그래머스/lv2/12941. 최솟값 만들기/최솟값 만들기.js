function solution(A,B){
    var answer = 0;
    
    const sortA = A.sort((a,b) => a-b);
    const sortB = B.sort((a,b) => b-a)
    
    for(const idx in sortA) {
        answer += sortA[idx] * sortB[idx]
    }

    return answer;
}