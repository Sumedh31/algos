var ar = [2,3,4,23,4,3,3]
var dict = {}
let pairs = 0;
ar.forEach((element) => {
    if(element in dict){
        dict[element]+=1;
    }
    else{
        dict[element]=1;
    }
});

for(let element in dict){
    if(dict[element]>1){
        pairs+=dict[element] % 2;
        //pairs+=Math.floor(dict[element] / 2);
    }
}
console.log(pairs)