
def insertNum(num: int,lis: list):
    #find the number directly below
    #print("num",num,"list",lis)
    if not lis:
        return [num] 
    if num <= lis[0]:
        return [num]+lis
    if num >= lis[-1]:
        return lis+[num]
    l,r,m = 0, len(lis)-1, 0
    while l < r:
        m = (l+r)//2
        if lis[m] < num:
            l = m + 1
        else:
            r = m
    lis.insert(l,num)
    return lis


def process1():
    listA, listB = [],[]
    with open('input.txt', 'r') as file:
        for line in file:
            a,b = str.split(line)
            listA = insertNum(int(a),listA)
            listB = insertNum(int(b),listB)
    check(listA,"listA")
    check(listB,"listB")

    result = 0
    for i in range(0,len(listA)):
        #print(listA[i],listB[i])
        result += abs(listA[i]-listB[i])
    return result

def process2():
    listA = []
    mapB = {}
    with open('input.txt', 'r') as file:
        for line in file:
            a,b = str.split(line)
            listA.append(a) 
            mapB[b] = mapB.get(b,0)+1

    result = 0
    for num in listA:
        result += mapB.get(num,0) * int(num)
    return result

def check(a,s):
    temp = a[:]
    temp.sort()
    if temp != a:
        print("a   ",a)
        print("temp",temp)
        errors = []
        for i in range(0,len(a)):
            if temp[i] != a[i]:
                errors = errors + [i]    
        print(s,"not sorted")
        print(errors[:100])
        return True 
    return False 

         

def testing():
    l = []
    l = insertNum(4,l)
    print("after 4",l)
    l = insertNum(6,l)
    print("after 6",l)
    l = insertNum(1,l)
    print("after 1",l)
    l = insertNum(3,l)
    print("after 3",l)
    l = insertNum(5,l)
    print("after 5",l)
    l = insertNum(8,l)
    print("after 8",l)

if __name__ == "__main__":
#    testing()
#    print(process1())
    print(process2())





