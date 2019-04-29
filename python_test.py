b=[]
for i in range(1,200):
    if(i%7==0) and (i%5!=0):
    b.append(str(i))
    print(','.join(b))
