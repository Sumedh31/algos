function checkPalindrome(input: string): boolean {
    let reversed: string = input.split('').reverse().join('');
    if (reversed == input){
        return true;
    }
    else {
        return false;
    }
}

console.log(`Check for ana - ${checkPalindrome('ana')}`)