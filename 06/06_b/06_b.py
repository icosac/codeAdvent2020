#Yeah... so my code works fine, simply the site is bugged.
def main():
    f=open("input.txt", "r")
    chars=[]
    persons=0
    res=0
    for line in f:
        if line!="\n":
            persons+=1
            for c in line:
                if c!="\n":
                    id=-1
                    i=0
                    while i<len(chars) and id==-1:
                        if c==chars[i]["c"]:
                            id=i
                        i+=1
                    if id==-1:
                        chars.append({"c":c, "v":1})
                    else:
                        chars[id]["v"]+=1
        else:
            for c in chars:
                if c["v"]==persons:
                    res+=1
            persons=0
            chars=[]
    print(res)
        
def main1():
    answers = 0
    group = []
    with open('input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line == '':
                # Idea for this line from: https://stackoverflow.com/a/2541814
                answers += len(set.intersection(*group))
                group = []
            else:
                group.append(set(line))
    print(f"Part 2 answer - N° yes answers: {answers}")


if __name__=="__main__":
    main1()

