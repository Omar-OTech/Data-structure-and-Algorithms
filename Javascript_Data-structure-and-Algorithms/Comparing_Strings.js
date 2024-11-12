let a = "hello";
let b = "world";
// To compare strings alphabetically, use the localeCompare() method.
// This return native value if the reference string is alphabetically before the compare string.
// return positive value if the reference string is alphabetically after the compare string.
console.log(a.localeCompare(b)); // -1

// use > and < operator to compare strings
const compareStr = (a, b) => {
    if ( a === b ) {
        return 0;
    }
    if ( a > b) {
        return 1;
    }
    return -1;
}

console.log(compareStr("hello", "world")); // -1
console.log(compareStr("hello", "hello")); // 1
console.log(compareStr("world", "hello")); // 1

let arr = ["hello", "world", "apple", "banana"];
arr.sort((a, b) => {
    return a.localeCompare(b);
});
console.log(arr); // [ 'apple', 'banana', 'hello', 'world' ]