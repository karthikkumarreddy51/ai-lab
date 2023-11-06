arrlist=[];
def move(board,goal,v):
    a=board.index('0')
    list={};
    if(a-3>-1):#top
        l1=board[:];
        temp=l1[a-3]
        l1[a-3]='0'
        l1[a]=temp
        if l1 not in arrlist:
            list["top"]=l1;
            arrlist.append(l1);
    if a not in [2,5,8]:#right
        l4=board[:];
        temp=l4[a+1]
        l4[a+1]='0'
        l4[a]=temp
        if l4 not in arrlist:
            list["right"]=l4;
            arrlist.append(l4)
    if(a+3<9):#bottom
        l2=board[:];
        temp=l2[a+3]
        l2[a+3]='0'
        l2[a]=temp
        if l2 not in arrlist:
            list["bottom"]=l2;
            arrlist.append(l2);
    if a not in [0,3,6]:#left
        l3=board[:];
        temp=l3[a-1]
        l3[a-1]='0'
        l3[a]=temp
        if l3 not in arrlist:
            list["left"]=l3;
            arrlist.append(l3)
    solve(list,goal,v)        
def solve(l,goal,v):
    c=[];
    value=list(l.values());
    side=list(l.keys());
    for i in value:
        if(i!=goal):
            count=v;
            for j in range(9):
                if i[j]!=goal[j]:
                    count+=1;
            c.append(count-1)
        else:
            print(side[value.index(i)],"==>",v,"+0")
            for k in range(0,9,3):
                print(i[k],i[k+1],i[k+2],sep=" ",end="\n");
            print("Goal state found")
            print("no.of states",v)
            return
    print(side[c.index(min(c))],"==>",v,"+",min(c)-v)
    for i in range(0,9,3):
          print(value[c.index(min(c))][i],value[c.index(min(c))][i+1],value[c.index(min(c))][i+2],sep=" ",end="\n");
    v+=1;    
    move(value[c.index(min(c))],goal,v)
initial=input("initial state").split(" ")
goal=input("goal state").split(" ")
move(initial,goal,1)