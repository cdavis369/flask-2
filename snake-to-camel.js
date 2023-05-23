function snakeToCamel(string) {
  let result = "";
  let toUpper = false;
  for (let c of string) {
    if (toUpper === true) {
      result += c.toUpperCase();
      toUpper = false;
    }
    else if (c === '_')
      toUpper = true;
    else
      result += c;
  }
  return result;
}

