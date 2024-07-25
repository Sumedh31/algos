function getCharCount(input) {
    let charDict = {};
    for(char in input){
        if(char in charDict){
            charDict[char]+=1;
        }
        else{
            charDict[char]=1
        }
    }
    return charDict
}

function isAnagram(firstWord, secondWord){
    let firstWordChar = getCharCount(firstWord);
    let secondWordChar = getCharCount(secondWord);

    console.log(`first word char length is ${Object.keys(firstWordChar).length}`)

    if(Object.keys(firstWordChar) != Object.keys(secondWordChar).legth){
        return false;
    }
    else{
        Object.keys(firstWordChar).forEach((key) => {
            if(secondWordChar[key]!=firstWordChar[key] || !secondWordChar.hasOwnProperty(key)){
                return false;
            }
        });
    }
}

console.log(`Check anagram of listen and silent ${isAnagram('listen','silent')}`);