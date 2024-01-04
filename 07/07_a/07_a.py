import re 

def main():
    l_colors=[]
    s_colors=["shiny gold"]
    i=0
    while len(s_colors)!=0:
        color=s_colors[0]
        f=open("input.txt", "r")
        for line in f:
            find=re.search("(.+) bags contain .*"+color+" bag.*", line)
            if find!=None:
                new_color=find.groups()[0]
                if new_color not in s_colors and new_color not in l_colors:
                    s_colors.append(new_color)
        l_colors.append(s_colors[0])
        s_colors=s_colors[1:]
        i+=1
            
    print(len(l_colors)-1)


if __name__=="__main__":
    main()
