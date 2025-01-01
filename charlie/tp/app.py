num_words = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90,'hundred':100,'thousand':1000,'million':1000000
}

inpu = 'charlie forty five and eighteen , haraz and hundred twenty one group one'

a=inpu.split()

L=[]
total = 0
i=0
while True:
    #try:
        if a[i] in num_words:
                total += num_words[a[i]]
                i+=1
                continue
        else:
            if a[i] == 'and' or a[i] == ',':
                if total != 0:
                    L.append(total)
                total = 0
                i+=1
                continue
            else:
                if total != 0:
                    L.append(total)
                L.append(a[i])
                total = 0
                i+=1
    except:
        L.append(total)
        total = 0
        break

print(a)        
print(L)