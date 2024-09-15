var year = (new Date()).getFullYear();
// console.log(year)
var time = (new Date()).getTime();
// console.log(time)
var month = (new Date()).getMonth();
// console.log(month)
var Day = (new Date()).getDate();
// console.log(Day)
var hours = (new Date()).getHours();
// console.log(hours)
var min = (new Date()).getMinutes();
// console.log(min)
var sec = (new Date()).getSeconds();
// console.log(sec)
console.log(`Today is ${Day}-${month+1}-${year} Time Now ${hours}:${min}:${sec}`);

var date = `Today is ${Day}-${month+1}-${year} Time Now ${hours}:${min}:${sec}`;

var res = document.getElementById('date');
res.innerHTML += `<p>${date}</p>`

