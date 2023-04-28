let redAllowEmptyCache = {}
let redNotAllowEmptyCache = {}
function red(n, allowEmpty = false) {
  if (n < 2) {
    return allowEmpty ? 1 : 0;
  }

  if (n === 2) {
    return allowEmpty ? 2 : 1;
  }

  if (allowEmpty) {
    if (redAllowEmptyCache[n] !== undefined) {
      return redAllowEmptyCache[n]
    }
    const result = red(n - 2, true) + red(n - 1, allowEmpty);
    redAllowEmptyCache[n] = result;
    return result;
  } else {
    if (redNotAllowEmptyCache[n] !== undefined) {
      return redNotAllowEmptyCache[n]
    }
    const result = red(n - 2, true) + red(n - 1, false);
    redNotAllowEmptyCache[n] = result;
    return result;
  }
}

let greenAllowEmptyCache = {}
let greenNotAllowEmptyCache = {}
function green(n, allowEmpty = false) {
  if (n < 3) {
    return allowEmpty ? 1 : 0;
  }

  if (n === 3) {
    return allowEmpty ? 2 : 1;
  }

  if (allowEmpty) {
    if (greenAllowEmptyCache[n] !== undefined) {
      return greenAllowEmptyCache[n]
    }
    const result = green(n - 3, true) + green(n - 1, allowEmpty);
    greenAllowEmptyCache[n] = result;
    return result;
  } else {
    if (greenNotAllowEmptyCache[n] !== undefined) {
      return greenNotAllowEmptyCache[n]
    }
    const result = green(n - 3, true) + green(n - 1, false);
    greenNotAllowEmptyCache[n] = result;
    return result;
  }
}

let blueAllowEmptyCache = {}
let blueNotAllowEmptyCache = {}
function blue(n, allowEmpty = false) {
  if (n < 4) {
    return allowEmpty ? 1 : 0;
  }

  if (n === 4) {
    return allowEmpty ? 2 : 1;
  }

  if (allowEmpty) {
    if (blueAllowEmptyCache[n] !== undefined) {
      return blueAllowEmptyCache[n]
    }
    const result = blue(n - 4, true) + blue(n - 1, allowEmpty);
    blueAllowEmptyCache[n] = result;
    return result;
  } else {
    if (blueNotAllowEmptyCache[n] !== undefined) {
      return blueNotAllowEmptyCache[n]
    }
    const result = blue(n - 4, true) + blue(n - 1, false);
    blueNotAllowEmptyCache[n] = result;
    return result;
  }
}

function total(n) {
  return red(n) + green(n) + blue(n)
}

console.log(total(50));
