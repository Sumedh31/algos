// Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

// function solution(intArray, target){
//     var indices = {}
//     var counter = 1;
//     for(var i = 0; i<intArray.length;i++){
//         for(var j=0;j<intArray.length;j++){
//             if(i!=j && intArray[i]+intArray[j] == target){
//                 if(!Object.values(indices).some(arr => arr.includes(i) && arr.includes(j))){
//                     indices[counter++]=[i,j];
//                 }                
//             }

//         }
//     }
//     return indices;
// }
// console.log(solution([2, 7, 11, 15], 9));

function getIndicesOfMatchingElementsOfTargetSum(intArray, target){
    var indices = {}
    var counter = 1;
    var seen = {}
    for(var i = 0; i<intArray.length;i++){
        var complement = target - intArray[i];
        if(seen.hasOwnProperty(complement)){
            indices[counter++] = [i,seen[complement]]            
        }
        seen[intArray[i]]=i;
    }
    return indices;
}
console.log(getIndicesOfMatchingElementsOfTargetSum([2, 7, 11, 15], 9));