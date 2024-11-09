// instanceof command;
// To find whether an object was constructed by a certain constructor or one inheriting from it
// can use the instanceof command
{/*
    I want this func to take the sum of the numbers passes to it
    */}
function sum(...arguments) {
    if (arguments.length === 1) {
        const [firstArg] = arguments
        if (firstArg instanceof Array) {
            return sum(...firstArg)
        }
    }
    return arguments.reduce((a, b) => a + b)
}

console.log(sum(1, 2, 3))
console.log(sum(1, 2, 3, 4, 5))
console.log(sum([1, 2, 3]))
console.log(sum(4))

