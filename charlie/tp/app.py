d = {}

for i in range(3):
    c_name = input("Enter country name:")
    cc_name = input("Enter captial:")
    courency = input("Enter courency:")
    d[c_name]=[cc_name,courency]
    

for i in d:
    print(f"| {i} | {d[i][0]} | {d[i][1]} |")
    
    