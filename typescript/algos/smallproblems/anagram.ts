

function getCharacterCount(input: string): {[key:string]: number}{
    let dict: {[key: string]: number } = {};

    for(const char of input) {
        if (!(char in dict)) {
            dict[char] = 1
        }
        else {
            dict[char]+=1
        }
    }
    return dict

}

function checkAnagram(first: string, second: string): boolean {
    let firstWord = getCharacterCount(first);
    let secondWord = getCharacterCount(second);

    if(firstWord.length !== secondWord.length) {
        return false
    }
    Object.keys(firstWord).forEach((key) => {
        if( secondWord[key] != firstWord[key] || !secondWord.hasOwnProperty(key)){
            return false
        }
    });
    return true;

}

console.log(`Does anagram exists for words silent and listen ? ${checkAnagram('silent', 'listen')}`)