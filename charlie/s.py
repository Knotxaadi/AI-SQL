L=['first_name','last_name','age']

s=input(":")
v=s.partition(",")
R=[]

for i in v:
    if i in L:
        R.append(i)
    
L=R
print(L)
