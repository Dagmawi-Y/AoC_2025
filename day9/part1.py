coords = []

# Parse input file
with open("input.txt", "r") as f:
    for line in f:
        if line.strip():
            x, y = map(int, line.strip().split(","))
            coords.append((x, y))

max_area = 0

# Compare every unique pair of points
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        p1, p2 = coords[i], coords[j]
        
        # Calculate dimensions (including starting tile)
        width = abs(p1[0] - p2[0]) + 1
        height = abs(p1[1] - p2[1]) + 1
        
        max_area = max(max_area, width * height)

print(max_area)
