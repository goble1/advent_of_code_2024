import re


def process2():
    total = 0
    memory = open("input.txt").read()
    on = True
    for match in re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))",memory): #r is a raw string
        if match == "do()":
            on = True
        elif match == "don't()":
            on = False
        elif on:
            x,y = map(int,match[4:-1].split(","))
            total += x*y
    return total 

def process1():
    total = 0
    memory = open("input.txt").read()
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)",memory): #r is a raw string
        x,y = map(int,match[4:-1].split(","))
        total += x*y
    return total 









         


if __name__ == "__main__":
    #print(process1())
    print(process2())





