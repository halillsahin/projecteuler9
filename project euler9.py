for a in range(1,1000):
    z=a*a
    for b in range(1,1000):
        y=b*b
        for c in range(1,1000):
            if z+y==(c*c) and a+b+c==1000:
                print(a*b*c) 
                break
                