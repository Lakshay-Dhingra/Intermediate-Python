import sys
t=int(input())
c=100
while(t):
    t=t-1
    
    x=0
    y=0
    print(f"Q {x} {y}",flush=True)
    d1=int(input())
    if(d1<0):
        sys.exit()
        
    x=c
    y=0
    print(f"Q {x} {y}",flush=True)
    d2=int(input())
    if(d2<0):
        sys.exit()
        
    x=0
    y=c
    print(f"Q {x} {y}",flush=True)
    d3=int(input())
    if(d3<0):
        sys.exit()
        
####################################################################    
    
    x12=((d1-d3)+c)
    y12=0
    print(f"Q {x12//2} {y12}",flush=True)
    x1=int(input())
    if(x1<0):
        sys.exit()
    x2=x12-x1
    
    x12=0
    y12=(d1-d2)+c
    print(f"Q {x12} {y12//2}",flush=True)
    y1=int(input())
    if(y1<0):
        sys.exit()
    y2=y12-y1
####################################################################
    print(f"A {y1} {x1} {y2} {x2}",flush=True)
    v=int(input())
    if(v<0):
        sys.exit()
