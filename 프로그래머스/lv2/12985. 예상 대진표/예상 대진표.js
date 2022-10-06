function solution(n,a,b)
{
    var answer = 0;
    let [ta, tb] = a > b ? [b,a] : [a,b]
    let i =0
    for(;i<parseInt(n / 2);i++) {
        if(tb-ta===0) {
            console.log(i)
            return i
        }
        ta = parseInt((ta +1) /2)
        tb = parseInt((tb +1)/2)
    }

    return i;
}