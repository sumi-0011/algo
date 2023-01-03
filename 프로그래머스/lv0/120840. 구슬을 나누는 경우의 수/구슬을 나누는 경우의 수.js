function solution(balls, share) {
    return Math.round(factorial(balls) / (factorial(balls - share) * factorial(share)));
    
    
}

function fac(number) {
    if(number === 0) return 1;
    return number * fac(number - 1)
}

function factorial(n) {
    res = 1
    for(let i =1;i<=n;i++) {
        res = res * i
    }
    return res
}