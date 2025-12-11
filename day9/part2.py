import sys
from collections import deque

coords = []
with open("input.txt", "r") as f:
    for line in f:
        if line.strip():
            x, y = map(int, line.strip().split(","))
            coords.append((x, y))


max_x = max(c[0] for c in coords) + 2
max_y = max(c[1] for c in coords) + 2


grid = [[0 for _ in range(max_x)] for _ in range(max_y)]


num_points = len(coords)
for i in range(num_points):
    p1 = coords[i]
    p2 = coords[(i + 1) % num_points] 
    
    
    if p1[0] == p2[0]: 
        start, end = min(p1[1], p2[1]), max(p1[1], p2[1])
        for y in range(start, end + 1):
            grid[y][p1[0]] = 1
    else: 
        start, end = min(p1[0], p2[0]), max(p1[0], p2[0])
        for x in range(start, end + 1):
            grid[p1[1]][x] = 1

queue = deque([(0, 0)])
seen = set([(0, 0)])


outside_mask = set()

while queue:
    cx, cy = queue.popleft()
    outside_mask.add((cx, cy))
    
    
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < max_x and 0 <= ny < max_y:
            
            if grid[ny][nx] == 0 and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((nx, ny))




P = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for y in range(max_y):
    for x in range(max_x):
        
        
        is_valid = 1 if (grid[y][x] == 1 or (x, y) not in outside_mask) else 0
        
        
        P[y+1][x+1] = is_valid + P[y][x+1] + P[y+1][x] - P[y][x]

def get_sum(x1, y1, x2, y2):
    
    return P[y2+1][x2+1] - P[y1][x2+1] - P[y2+1][x1] + P[y1][x1]


max_area = 0

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        p1 = coords[i]
        p2 = coords[j]
        
        
        x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
        y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
        
        width = (x2 - x1) + 1
        height = (y2 - y1) + 1
        target_area = width * height
        
        
        actual_valid_tiles = get_sum(x1, y1, x2, y2)
        
        
        if actual_valid_tiles == target_area:
            if target_area > max_area:
                max_area = target_area

print(max_area)