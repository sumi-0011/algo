function solution(s) {
    var answer = '';
    const arr = s.split(' ').map((str) => parseInt(str))
    console.log(Math.min(arr))
    return Math.min(...arr)+ " " +Math.max(...arr);
}