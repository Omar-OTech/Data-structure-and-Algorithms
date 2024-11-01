// DOM API

let p = document.getElementById("paragraph").textContent = "Hello, World!";

let element = document.createElement('h2');
element.textContent = "Hello, World! -> From h2";
document.body.appendChild(element);

// alert
// alert('Pause');
// console.log('Alert was dismissed');

// Prompt
// let name = prompt("Enter your name");
// let age = prompt("How old are you?");
// console.log(`Hello ${name}, your age is ${age}`);

// Window.confirm -> it is typically used to ask for user confirmation before doing a dangerous operation like deleting something.

if (window.confirm("Are you sure you want to delete this?")) {
    deleteItem(itemId);
}

