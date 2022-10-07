function solution(s) {
    const arr = s.split(' ')
    const answer = []
    for(const str of arr) {
    const first = str.charAt(0).toUpperCase()
        const etc = str.substring(1).toLowerCase()
        answer.push( first + etc )
    }
    console.log(answer )
    return answer.join(' ');
}