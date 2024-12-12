let counter = 1;

setInterval=(function () {
    console.log(counter++);
}, 1000);

setTimeout(function () {
    clearInterval(intervalId)
}, 5000);