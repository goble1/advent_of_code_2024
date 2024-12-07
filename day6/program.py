
def process1():
    grid = list(map(list, open("input.txt").read().splitlines()))
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                break #this break triggers the next break
        else:
            continue
        break
    dr, dc = -1, 0 
    seen = set() 
    while True:
        seen.add((r,c))
        if r+dr < 0 or r+dr == rows or c+dc < 0 or c+dc == cols: break
        if grid[r+dr][c+dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
    return len(seen) 

def process2():
    grid = list(map(list, open("input.txt").read().splitlines()))
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                break #this break triggers the next break
        else:
            continue
        break
    def loops(grid,r,c):
        dr, dc = -1, 0 
        seen = set() 
        while True:
            seen.add((r,c, dr,dc))
            if r+dr < 0 or r+dr == rows or c+dc < 0 or c+dc == cols: return False 
            if grid[r+dr][c+dc] == "#":
                dc, dr = -dr, dc
            else:
                r += dr
                c += dc
            if (r,c,dr,dc) in seen:
                return True
    count = 0
    for cr in range(rows):
        for cc in range(cols):
            if grid[cr][cc] != ".": continue
            grid[cr][cc] = "#"
            if loops(grid,r,c):
                count += 1
            grid[cr][cc] = "."
    return count

            

if __name__ == "__main__":
    print(process2())





