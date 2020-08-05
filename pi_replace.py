def convert(li,n,i):
    if(i==n-2):
        if(li[i]=='p' and li[i+1]=='i'):
            li[i]='3'
            li[i+1]='.'
            li.append('1')
            li.append('4')
            n=n+2
        return li
    else:
        li=convert(li,n,i+1)
        if(li[i]=='p' and li[i+1]=='i'):
            li[i]='3'
            li[i+1]='.'
            li.insert(i+2,'1')
            li.insert(i+3,'4')
            n=n+2
        return li
s=input()
li=list(s)
print(s)
print("".join(convert(li,len(li),0)))
