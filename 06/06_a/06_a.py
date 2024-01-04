def main():
    f=open("input.txt", "r")
    group=[]
    res=0
    for line in f:
        if line=="\n":
            res+=len(group)
            group=[]
        else:
            for c in line:
                if c not in group and c!="\n":
                    group.append(c)
    print(res)



if __name__=="__main__":
    main()
