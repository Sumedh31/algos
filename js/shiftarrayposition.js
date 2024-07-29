// //Given an array, rotate it to the right by k steps, where k is non-negative.
// function rotateArray(intArray,position){
//     console.log(int);
//     var toRotate = intArray.splice(-position,position);
//     console.log(toRotate);
//     intArray.unshift(...toRotate);
//     return intArray;
// }

// console.log(rotateArray([1, 2, 3, 4, 5, 6, 7],3));

//Given an array, rotate it to the right by k steps, where k is non-negative.
function rotateArray(intArray,position){
    console.log(intArray);
    var toRotate = intArray.splice(0,position);
    intArray.push(...toRotate);
    return intArray;
}

console.log(rotateArray([1, 2, 3, 4, 5, 6, 7],3));