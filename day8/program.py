
def process1():
    grid = [ line.strip() for line in open("input.txt") ]
    rows, cols = len(grid), len(grid[0])
    anennas = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != ".":
                if char not in anennas: anennas[char] = []
                anennas[char].append((r,c))
    antinode = set() 
    for array in anennas.values():
        for i in range(len(array)):
            for j in range(i+1,len(array)):
                r1,c1 = array[i]
                r2,c2 = array[j]
                antinode.add((2*r1-r2,2*c1-c2))
                antinode.add((2*r2-r1,2*c2-c1))
                
    return len([0 for r,c in antinode  if 0 <= r < rows and 0 <= c < cols])
    #print(len([0 for r,c in antinodes if 0 <= r < rows and 0 <= c < cols]))
if __name__ == "__main__":
    print(process1())





