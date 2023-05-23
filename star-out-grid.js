function starOutGrid(grid) {
  let starCount = m = n = 0;
  let stars = {}
  
  for (m = 0; m < grid.length; m++) {
    for (n = 0; n < grid[m].length; n++) {
      if (grid[m][n] === "*") {
        starCount++;
        stars[starCount] = {"row": m, "col": n}
      }
    }
  }
  
  for (let s in stars) 
    starReplace(grid, stars[s]["row"], stars[s]["col"]);
  
  return grid;
} 

function starReplace(grid, m, n) {
  // console.log(grid, m, n);
  for (let col = 0; col < grid[m].length; col++)
    grid[m][col] = "*";

  for (let row = 0; row < grid.length; row++)
    grid[row][n] = "*";
}

