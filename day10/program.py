from collections import deque

def process1():
    grid = [[int(char) for char in line.strip()] for line in open(0)]

    rows = len(grid)
    cols = len(grid[0])

    zeros = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]


    
    def score(grid,r,c):
        q = deque([(r, c)])
        seen = {(r, c)}
        summits = 0
        while len(q) > 0:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if grid[nr][nc] != grid[cr][cc] + 1: continue
                if (nr, nc) in seen: continue
                seen.add((nr, nc))
                if grid[nr][nc] == 9:
                    summits += 1
                else:
                    q.append((nr, nc))
        return summits

    return sum(score(grid, r, c) for r, c in zeros);

def process2():
    grid = [[int(char) for char in line.strip()] for line in open(0)]
    rows = len(grid)
    cols = len(grid[0])
    trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    def score(grid, r, c):
        q = deque([(r, c)])
        seen = {(r, c): 1}
        trails = 0
        while len(q) > 0:
            cr, cc = q.popleft()
            if grid[cr][cc] == 9:
                trails += seen[(cr, cc)]
            for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if grid[nr][nc] != grid[cr][cc] + 1: continue
                if (nr, nc) in seen:
                    seen[(nr, nc)] += seen[(cr, cc)]
                    continue
                seen[(nr, nc)] = seen[(cr, cc)]
                q.append((nr, nc))
        return trails
    return sum(score(grid, r, c) for r, c in trailheads)

if __name__ == "__main__":
    print(process2())





