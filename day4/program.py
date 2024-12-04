import re


def process2():
    total = 0
    grid = open("input.txt").read().splitlines()
    for r in range(1,len(grid)-1):
        for c in range(1,len(grid[0])-1):
            if grid[r][c] != "A": continue
            #          up left         down left      down right     up right
            corners =  [grid[r-1][c-1],grid[r+1][c-1],grid[r+1][c+1],grid[r-1][c+1]]
            if "".join(corners) in ["MMSS","SMMS","SSMM","MSSM"]:
                total += 1
    return total

def process1():
    total = 0
    grid = open("input.txt").read().splitlines()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != "X": continue
            #print(grid[r][c])
            #for dr, dc in [(-1,0),(-1,1),(-1,-1),(1,0),(1,1),(1,-1),(0,-1),(0,1)]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == dc == 0: continue
                    if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])): continue
                    if grid[r+dr][c+dc] == "M" and grid[r+dr*2][c+dc*2] == "A" and grid[r+dr*3][c+dc*3] == "S": 
                        total += 1

    return total 









         


if __name__ == "__main__":
    #print(process1())
    print(process2())





