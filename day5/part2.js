const fs = require("fs");

function solve() {
  const raw = fs.readFileSync("input.txt", "utf8").trimEnd();

  // only need the first block now
  const [rangesPart] = raw.split(/\n\s*\n/);
  const rangeLines = rangesPart.split("\n");

  console.log(countTotalFresh(rangeLines));
}

function countTotalFresh(rangeLines) {
  const ranges = rangeLines.map(line => {
    const [a, b] = line.split("-").map(Number);
    return { start: a, end: b };
  });

  // merge
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

  // now sum lengths
  let total = 0;
  for (const r of merged) {
    total += (r.end - r.start + 1);
  }

  return total;
}

solve();
