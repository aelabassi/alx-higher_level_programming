#!/usr/bin/node
function Factorial (n) {
  if (n < 0) {
    return (-1);
  } else if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}
console.log(Number(Factorial(process.argv[2])));
