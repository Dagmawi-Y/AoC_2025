const fs = require("fs");

function solve() {
  const raw = fs.readFileSync("input.txt", "utf8").replace(/\r/g, "");
  const lines = raw.split("\n");

  const W = Math.max(...lines.map(l => l.length));
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
  flushCurrent();
  problems.reverse(); // p2 is rtl reading

  let total = 0;
  for (const cols of problems) {
    total += evalProblem(cols);
  }

  console.log(total);

  function flushCurrent() {
    if (currentCols.length === 0) return;
    problems.push(currentCols);
    currentCols = [];
  }
}

function evalProblem(cols) {
  const H = cols[0].length;

  // find bottom operator
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

  // read each column above operator as a number (top to bottom)
  let numbers = [];
  for (let c = 0; c < cols.length; c++) {
    let digits = "";
    for (let r = 0; r < opRow; r++) digits += cols[c][r];
    digits = digits.trim();
    if (digits.length > 0) numbers.push(parseInt(digits, 10));
  }

  // fold
  let result = op === "+" ? 0 : 1;
  for (let n of numbers) {
    if (op === "+") result += n;
    else result *= n;
  }

  return result;
}

solve();
