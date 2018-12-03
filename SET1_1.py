x=int(input())
m=list(map(int,input().strip().split()))
n=list(set(m))
if(len(m)!=len(n)):
    for i in n:
        if(m.count(i)>1):
            print(i,end=" ")
else:
    print("unique")
    
    
