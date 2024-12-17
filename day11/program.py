from functools import cache

def process1():
    input = [int(i) for i in open("input.txt").readline().split()]
    return split_stones(input,25)
    

def split_stones(stones,iterations):
    for _ in range(iterations):
        temp = []
        for stone in stones:
            if stone == 0:
                temp.append(1)
                continue
            string = str(stone)
            length = len(string)
            if length % 2 == 0:
                temp.append(int(string[:length//2]))
                temp.append(int(string[length//2:]))
            else:
                temp.append(stone*2024)
        stones = temp
    return len(stones)

@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1,steps-1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length//2]),steps-1) + count(int(string[length//2:]),steps-1)
    else:
        return count(stone*2024,steps-1)
    
def process2():
    stones = [int(i) for i in open("input.txt").readline().split()]
    return sum(count(stone,75) for stone in stones) 

     

if __name__ == "__main__":
    print(process2())





