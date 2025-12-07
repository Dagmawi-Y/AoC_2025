const fs = require("fs");

function solve() {
  const raw = fs.readFileSync("input.txt", "utf8").replace(/\r/g, "");
  const lines = raw.split("\n");

  // width
  const W = Math.max(...lines.map(l => l.length));

  // normalize each line to width with spaces
  const grid = lines.map(l => l.padEnd(W, " "));

  let problems = [];
  let currentCols = [];

  for (let c = 0; c < W; c++) {
    const col = grid.map(row => row[c]);
    const isBlank = col.every(ch => ch === " ");

    if (isBlank) {
      flushCurrent();
    } else {
      currentCols.push(col);
    }
  }
  flushCurrent(); // flush last

  function flushCurrent() {
    if (currentCols.length === 0) return;
    problems.push(currentCols);
    currentCols = [];
  }

  // parse each problem
  let total = 0;
  for (const cols of problems) {
    total += evalProblem(cols);
  }

  console.log(total);
}

function evalProblem(cols) {
  // read columns as a block
  const H = cols[0].length;

  // find bottom op (first non-space from bottom)
  let op = null;
  let opRow = null;
  for (let r = H - 1; r >= 0; r--) {
    for (let c = 0; c < cols.length; c++) {
      const ch = cols[c][r];
      if (ch === "+" || ch === "*") {
        op = ch;
        opRow = r;
        break;
      }
    }
    if (op) break;
  }

  if (!op) throw new Error("no op found");

  // extract numbers above opRow
  // each number is formed by reading the entire row across columns
  let numbers = [];
  for (let r = 0; r < opRow; r++) {
    let rowStr = "";
    for (let c = 0; c < cols.length; c++) rowStr += cols[c][r];
    rowStr = rowStr.trim();
    if (rowStr.length > 0) {
      numbers.push(parseInt(rowStr, 10));
    }
  }

  let result = op === "+" ? 0 : 1;
  for (let n of numbers) {
    if (op === "+") result += n;
    else result *= n;
  }

  return result;
}

solve();
