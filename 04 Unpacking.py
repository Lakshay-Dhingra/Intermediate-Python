#Unpacking Sequence data structure

li=["ram",0,3.5,[1,2,3,4]]
print(li)
first,second,third,fourth=li
print(first,second,third,fourth)

tp=tuple(li)
print(tp)
first,second,third,fourth=tp
print(first,second,third,fourth)

st=set([1,2,3,5])
print(st)
first,second,third,fourth=st
print(first,second,third,fourth)

di={1:"hello", 2:"world"}
first,second=di
print(first,second)
