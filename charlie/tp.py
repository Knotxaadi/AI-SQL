import csv 
from tabulate import tabulate

mf = open(r'C:\rti form\cs\AI-SQL\charlie\trial.csv','r+')

w= csv.writer(mf,delimiter=',')
r = csv.reader(mf,delimiter=',')

L=[]
for i in r:
    L.append(i)

h = ['name','lastname','age']

print(tabulate(L, h, tablefmt="rounded_grid"))
mf.close()
