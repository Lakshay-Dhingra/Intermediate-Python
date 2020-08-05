t=int(input())
n=list(input() for i in range(t))
def f(x):
    fact=int(1)
    if x==0:
      return 1  
    while(x>0):
        fact=fact*x
        x=x-1
    return fact
for i in range(t):
    print(f(int(n[i])))
