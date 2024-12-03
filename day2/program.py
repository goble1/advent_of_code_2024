


def process1():
    result = 0
    with open('input.txt', 'r') as file:
        for line in file:
            reportsStr = str.split(line)
            reports = [int(x) for x in reportsStr]
            safe = 1
            if reports[0] > reports[1]: #decreasing
                for i in range(1,len(reports)):
                    if reports[i-1] <= reports[i] or reports[i-1]-reports[i]>3:
                        safe = 0
                        break
            else: #increasing
                for i in range(1,len(reports)):
                    if reports[i-1] >= reports[i] or reports[i]-reports[i-1]>3:
                        safe = 0
                        break
            print("line:",i,"nums:",reports,"is:",safe)
            result += safe
    return result

def decreasing(reports: list):
    safe = 1
    errors = 0
    prev = reports[0]
    for i in range(1,len(reports)):
        if prev <= reports[i] or prev-reports[i]>3:
            if errors == 1:
                safe -= 1
                break
            else:
                errors += 1
        else:
            prev = reports[i]
    #print("line:",reports,"safe:",safe)
    if safe > 0:
        return 1
    return 0

def increasing(reports: list):
    safe = 1
    errors = 0
    prev = reports[0]
    for i in range(1,len(reports)):
        if prev >= reports[i] or reports[i]-prev>3:
            if errors == 1:
                safe -= 1
                break
            else:
                errors += 1
        else:
            prev = reports[i]
    #print("line:",reports,"safe:",safe)
    if safe > 0:
        return 1
    return 0

def safe( reports: list):
    diffs = [x - y for x,y in zip(reports[1:],reports)]
    return all(1<= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)


def process2():
    result = 0
    with open('input.txt', 'r') as file:
        for line in file:
            reportsStr = str.split(line)
            levels = [int(x) for x in reportsStr]
            if any(safe(levels[:i]+levels[i+1:]) for i in range(len(levels))):
                result += 1
    return result






         


if __name__ == "__main__":
    #print(process1())
    print(process2())





