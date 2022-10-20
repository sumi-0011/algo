function solution(sides) {
    var answer = 0;
    
    const max = Math.max(...sides)
    const other = sides.filter(side => side != max)
    
    console.log(max, other)
    if(other[0]+other[1] <= max) return 2
    
    return 1;
}