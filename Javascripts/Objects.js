// An Object is a group of values; unlike arrays.

john = {firstname: "John", lastname: "Doe", age: 35, fullname: "John Doe"};
billy = {firstname: "Billy", lastname: undefined, age: 40, fullname: "Billy"};

// window.alert(john.fullname);
console.log(john.age);
// window.alert(billy.fullname);
console.log(billy.age);

function printInfo(person) {
    console.log(person.firstname);
    console.log(person.lastname);
    console.log(person.age);
    console.log(person.fullname);
}

printInfo({firstname: "John", lastname: "Doe", age: 35, fullname: "John Doe"});
printInfo({firstname: "Billy", lastname: undefined, age: 40, fullname: "Billy"});