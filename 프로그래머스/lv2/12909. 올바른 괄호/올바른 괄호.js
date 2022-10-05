function solution(s){
    var answer = true;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')
    const arr  = s.split('')
    const stack = []
    for(const str of arr) {
        if(str === '(') {
            stack.push(str)
        }
        else {
            if(stack.length ===0 ) return false
            stack.pop();
        }
    }
    console.log(stack)
    if(stack.length === 0) {
        return true}
    else {
        return false
    }
}