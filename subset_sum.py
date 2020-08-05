def countsum(step,li,k,n):
    if(step==n):
        count=0
        if(sum(li)==k):
            count+=1
        return count
    else:
        count=countsum(step+1,li,k,n)
        for i in range(n-step):
            if(sum(li[i:i+step])==k):
                count+=1
        return count
k=int(input())
li=list(map(int,input().split()))
print(countsum(1,li,k,len(li)))
