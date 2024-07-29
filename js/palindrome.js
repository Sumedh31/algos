function isPalindrome(input){
    // let revrsed = input.split('').reverse().join('');
    // if(input == revrsed){
    //     console.log('Its palindrome');
    // } 
    let reversed = [];
    for(var i=input.length-1;i>=0;i--){
        reversed.push(input[i]);
    }
    console.log(reversed);
    let reveresedInput = reversed.join('');
    let status = input==reveresedInput?'The string is palindrome':'Its Not palindromer';
    console.log(`${status}`)
}
isPalindrome('ana');