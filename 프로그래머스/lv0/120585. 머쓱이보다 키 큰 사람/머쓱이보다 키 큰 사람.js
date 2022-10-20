function solution(array, height) {
    var answer = 0;
    
    const filter = array.filter((ar) => ar > height)
    return filter.length;
}