let canvas = document.createElement('canvas');
canvas.width = 500;
canvas.height = 250;

// selecte conttext of canvas
let ctx = canvas.getContext('2d');

// Set properties related to the text
ctx.font = "30px Cursive";
ctx.fillText("Hello, World", 125, 125);

document.body.appendChild(canvas);