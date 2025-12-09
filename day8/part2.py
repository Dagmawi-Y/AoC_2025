import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_sets = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_sets -= 1
            return True
        return False

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
    if n < 2:
        print("Not enough points to form connections.")
        return

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2
            edges.append((dist_sq, i, j))

    edges.sort(key=lambda x: x[0])

    dsu = DSU(n)

    for _, u, v in edges:
        if dsu.union(u, v):
            if dsu.num_sets == 1:
                p_u = points[u]
                p_v = points[v]
                
                # the problem asks for the product of the X coordinates
                result = p_u[0] * p_v[0]
                
                print(f"final connection formed between {p_u} and {p_v}")
                print(f"product of X coordinates: {result}")
                return

if __name__ == "__main__":
    solve()