const fib = (n,memo = {}) => {
  if (n in memo) return memo[n] //Retrieve result for index if previously calculated
  if (n <= 2) return 1; //Base case
  memo[n] = fib(n-2)+fib(n-1) //Store sum of current sum
  return memo[n] 
}

/*
Less recursive calls due to fetching of values = Better perfomance
Time complexity = 
Space Complexity = 
*/