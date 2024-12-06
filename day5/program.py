import functools

def process1():
    total = 0
    file = open("input.txt")
    rules = []
    #page rules
    for line in file:
        if line.isspace(): break
        rules.append(list(map(int,line.split("|"))))
    
    #cache for all the comparison
    cache = {}
    for x,y in rules:
        cache[(x,y)] = True
        cache[(y,x)] = False

    def is_ordered(update):
        for i in range(len(update)):
            for j in range(i+1,len(update)):
                key=(update[i],update[j])
                if key in cache and not cache[key]:
                    return False 
        return True

            
    #go through pages
    for line in file:
        updates = list(map(int,line.split(",")))
        #check all of them
        if is_ordered(updates):
            total += updates[len(updates)//2]

    return total 

def process2():
    total = 0
    file = open("input.txt")
    rules = []
    #page rules
    for line in file:
        if line.isspace(): break
        rules.append(list(map(int,line.split("|"))))
    
    #cache for all the comparison
    cache = {}
    for x,y in rules:
        cache[(x,y)] = -1 
        cache[(y,x)] = 1 

    def cmp(x,y):
        return cache.get((x,y),0)

    def is_ordered(update):
        for i in range(len(update)):
            for j in range(i+1,len(update)):
                key=(update[i],update[j])
                if key in cache and cache[key] == 1 :
                    return False 
        return True

            
    #go through pages
    for line in file:
        update = list(map(int,line.split(",")))
        #check all of them
        if is_ordered(update): continue
        update.sort(key=functools.cmp_to_key(cmp))
        total += update[len(update)//2]


    return total 
if __name__ == "__main__":
    #print(process1())
    print(process2())





