function solution(brown, yellow) {
    var answer = [];
    
    const brownSide = (brown - 4) /2
    
    for(let i =1 ; i<= parseInt(brownSide/2) ;i++ ) {
        const w = i
        const h = brownSide - i
        if(w * h === yellow)
            return [h + 2, w + 2]
    }
    return answer;
}