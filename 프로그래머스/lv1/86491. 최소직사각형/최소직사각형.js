function solution(sizes) {
    var answer = 0;
    
    let Max1 = 1
    let Max2 = 1
    
    for(const [w, h] of sizes) {
        const [cMin, cMax] = w > h ? [h,w] : [w,h]
        if(Max1 < cMax) {
            Max1 = cMax
        }
        if(Max2 < cMin) {
            Max2 = cMin
        }
    }
    console.log(Max1, Max2)
    return Max1 * Max2;
}