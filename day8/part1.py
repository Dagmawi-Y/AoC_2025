import sys

def solve():
    
    points = []
    try:
        with open("input.txt", "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    points.append(tuple(map(int, parts)))
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    n = len(points)
    
    
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
            edges.append((dist_sq, i, j))

    
    edges.sort(key=lambda x: x[0])

    
    parent = list(range(n))
    size = [1] * n

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        
        if root_i != root_j:
            
            
            parent[root_i] = root_j
            size[root_j] += size[root_i]
            return True
        return False

    
    limit = 1000
    
    
    
    
    for k in range(min(limit, len(edges))):
        _, u, v = edges[k]
        union(u, v)

    
    
    circuit_sizes = []
    for i in range(n):
        if parent[i] == i:
            circuit_sizes.append(size[i])

    
    circuit_sizes.sort(reverse=True)

    
    if len(circuit_sizes) >= 3:
        result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
        print(f"sizes of top 3 circuits: {circuit_sizes[0]}, {circuit_sizes[1]}, {circuit_sizes[2]}")
        print(f"product: {result}")
    else:
        
        import math
        print(f"less than 3 circuits found. Sizes: {circuit_sizes}")
        print(f"product: {math.prod(circuit_sizes)}")

if __name__ == "__main__":
    solve()