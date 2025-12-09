def count_splits(grid):
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

    beams = [(start[0] + 1, start[1])]
    splits = 0
    visited = set()

    while beams:
        new_beams = []
        for r, c in beams:
            if r >= rows or c < 0 or c >= cols:
                continue

            if (r, c) in visited:
                continue
            visited.add((r, c))

            cell = grid[r][c]

            if cell == ".":
                new_beams.append((r+1, c))

            elif cell == "^":
                splits += 1
                new_beams.append((r+1, c-1))
                new_beams.append((r+1, c+1))

            else:
                new_beams.append((r+1, c))

        beams = new_beams

    return splits


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [list(line.rstrip("\n")) for line in f]

    print(count_splits(lines))
