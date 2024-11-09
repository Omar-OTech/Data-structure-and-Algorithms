// String
console.log(Object.prototype.toString.call('String'));

// Number
console.log(Object.prototype.toString.call(42));

// Bool
console.log(Object.prototype.toString.call(true));

// Object
console.log(Object.prototype.toString.call(Object()));
// Or
console.log(Object.prototype.toString.call());

// Function
console.log(Object.prototype.toString.call(function(){}));
console.log(Object.prototype.toString.call(() => {}));

// Date
console.log(Object.prototype.toString.call(new Date(2015,5,5)));

// Regex
console.log(Object.prototype.toString.call(new RegExp()));
// Or
console.log(Object.prototype.toString.call(/foo/));

// Array
console.log(Object.prototype.toString.call([]));

// Null
console.log(Object.prototype.toString.call(null));

// Undefined
console.log(Object.prototype.toString.call(undefined));

// Error
console.log(Object.prototype.toString.call(Error()));