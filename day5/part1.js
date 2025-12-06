const fs = require("fs");

function solve() {
  const raw = fs.readFileSync("input.txt", "utf8").trimEnd();

  // split at the blank line
  const [rangesPart, idsPart] = raw.split(/\n\s*\n/);

  const rangeLines = rangesPart.split("\n");
  const idLines = idsPart.split("\n");

  console.log(countFresh(rangeLines, idLines));
}

function countFresh(rangeLines, idLines) {
  const ranges = rangeLines.map(line => {
    const [a, b] = line.split("-").map(Number);
    return { start: a, end: b };
  });

  // merge ranges
  ranges.sort((a, b) => a.start - b.start);
  const merged = [];
  for (const r of ranges) {
    if (merged.length === 0 || r.start > merged[merged.length - 1].end) {
      merged.push({ ...r });
    } else {
      merged[merged.length - 1].end = Math.max(
        merged[merged.length - 1].end,
        r.end
      );
    }
  }

  // parse ids
  const ids = idLines.map(Number);

  // count fresh
  let count = 0;
  for (const id of ids) {
    if (isFresh(id, merged)) count++;
  }

  return count;
}

function isFresh(id, merged) {
  for (const r of merged) {
    if (id >= r.start && id <= r.end) return true;
    if (id < r.start) break;
  }
  return false;
}

solve();
