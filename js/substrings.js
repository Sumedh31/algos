function getSubStrings(input){
    for(var i =0;i<input.length;i++){
        for(var j= i+1; j<=input.length;j++){
            console.log(input.substring(i,j));
        }
    }
}
getSubStrings('ABC')