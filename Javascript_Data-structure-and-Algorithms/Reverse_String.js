const reverseString = (str) => {
    return str.split("").reverse().join('');
}
console.log(reverseString('string'));
console.log(reverseString('reversed'));

// console.log(String.prototype.split(deliminator)); // ['s', 't', 'r', 'i', 'n', 'g']
// console.log(Array.prototype.reverse())           // ['g', 'n', 'i', 'r', 't', 's']
// console.log(Array.prototype.join( deliminator)) //  "gnirts"


// use spread operator
const reverseStr = (str) => {
    return [...String(str)].reverse().join('')
}

console.log(reverseStr('javascript'));
console.log(reverseStr(1337));
console.log(reverseStr([1, 2, 3]));


// Custom reverse() Function
// const revStr = (str) => {
//     var strRev = ''
//     for (var i = str.length - 1; i >= 0; i++) {
//         strRev += String[i];
//     }
//     return strRev;
// }

// console.log(revStr('xyz'));