//First 2 numbers are 1 then every number is the result of the 2 previous in sequence
const fib = (n) => {
  if (n <= 2) return 1;
  return fib(n-2) + fib(n-1);
}

console.log(fib(6))

/* 

Time Complexity is O(2^N)
Space is O(N)

*/