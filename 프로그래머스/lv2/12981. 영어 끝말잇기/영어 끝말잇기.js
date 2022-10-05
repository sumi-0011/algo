function solution(n, words) {
    var answer = [];
    let cnt = -1
    let last = words[0].charAt(0);
    for(const idx in words) {
        const currentFirst = words[idx].charAt(0);
        const prev = words.slice(0,idx)
        const isExist = prev.findIndex((word) => word === words[idx])
        
        if(last === currentFirst && isExist == -1) {
            last = words[idx].charAt(words[idx].length -1)
        }
        else {
            cnt = idx
            console.log(idx)
            break;
        }
        
    }
    if(cnt === -1) {
        return [0,0]
    }else {
        const count = +cnt + 1
        const f =(count % n )===0 ? n : (count % n )
        const t = Math.ceil(count / n)
        return [f,t]
    }
    
}