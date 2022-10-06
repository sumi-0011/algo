function solution(babbling) {
    var answer = 0;
    for(const ba of babbling) {
        let temp = ba
        for(const word of ["aya", "ye", "woo", "ma"]) {
            const exit = temp.includes(word+word)
            if(exit) break
            const sArr = temp.split(word)
            temp = sArr.join('')
        }
        console.log(ba, temp)
        if(temp.length ===0) {
            answer +=1
        }
    }
    return answer;
}