function isAllUnique(input){
    let chars = [];
    for(const char of input){
        if(!chars.includes(char)){
            chars.push(char);
        }
        else{
            console.log(`Somethings wrong - ${input}`)
            return false;
        }
    }
    return true;
}

function longestSubstring(input){
    let longestSubStr = '';
    for(let i =0; i<input.length;i++){
        for(let j=i+1; j<=input.length;j++){
            let tempString = input.substring(i,j);
            console.log(`Temp String is - ${tempString}`)
            
            if(longestSubStr.length < tempString.length && isAllUnique(tempString)){
                longestSubStr = tempString;
            }
        }
    }
    console.log(`String is - ${longestSubStr}`)
    return longestSubStr;
}

console.log(longestSubstring('abcabcbb'))