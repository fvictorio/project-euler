let cache = {};
function f(n) {
  if (n === 0) {
    return 1;
  }

  if (n === 1) {
    return 1;
  }

  if (cache[n] !== undefined) {
    return cache[n];
  }

  let result = 0;

  // leave the first square empty
  result += f(n - 1);

  if (n >= 2) {
    result += f(n - 2);
  }
  if (n >= 3) {
    result += f(n - 3);
  }
  if (n >= 4) {
    result += f(n - 4);
  }

  cache[n] = result;
  return result;
}

console.log(f(50));
