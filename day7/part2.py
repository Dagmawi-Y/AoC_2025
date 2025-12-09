from typing import List

def read_grid(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.rstrip("\n") != ""]
    if not lines:
        raise ValueError("input.txt is empty")
    width = max(len(l) for l in lines)
    # normalize to rectangle (pad with dots)
    return [list(l.ljust(width, ".")) for l in lines]

def count_timelines(grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    # find S
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
                break
        if start:
            break
    if not start:
        raise ValueError("No 'S' found in the grid")

    row_start = start[0] + 1
    if row_start >= rows:
        return 1

    counts = [0] * cols
    counts[start[1]] = 1

    total_exited = 0

    # process rows from row_start to last row
    for r in range(row_start, rows):
        cur = counts[:]
        changed = True
        while changed:
            changed = False
            for c in range(cols):
                if cur[c] > 0 and grid[r][c] == "^":
                    v = cur[c]
                    cur[c] = 0
                    # left
                    if c - 1 >= 0:
                        cur[c - 1] += v
                    else:
                        total_exited += v
                    # right
                    if c + 1 < cols:
                        cur[c + 1] += v
                    else:
                        total_exited += v
                    changed = True

        # after stabilization, remaining particles fall down one row (or exit out bottom)
        next_counts = [0] * cols
        for c in range(cols):
            v = cur[c]
            if v == 0:
                continue
            if r + 1 < rows:
                next_counts[c] += v
            else:
                # falls out of bottom -> count as exited timelines
                total_exited += v

        counts = next_counts

    return total_exited

if __name__ == "__main__":
    grid = read_grid("input.txt")
    result = count_timelines(grid)
    print(result)
