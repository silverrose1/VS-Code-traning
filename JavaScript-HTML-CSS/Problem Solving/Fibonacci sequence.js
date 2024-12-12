// https://www.netacad.com/content/jse1/1.0/courses/content/m5/en-US/assets/0e57f80072f33cf5dc1a8879fdd87b47e3c5e871.png

function fib(n){
    if (n <= 1){
        return n;
    }
    else{
        return fib(n-1) + fib(n-2);
    }
}
console.log(fib(6));
