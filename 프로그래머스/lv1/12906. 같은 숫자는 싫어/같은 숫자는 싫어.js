function solution(arr)
{
    var answer = [];
    let last = -1
    for(const a of arr) {
        if(last === a) continue
        else {
            answer.push(a)
            last = a
        }
    }
    
    return answer;
}