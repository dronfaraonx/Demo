def hist(items):
    for i in items:
        outut = ""
        times = i
        while times>0:
            outut += "*"
            times -=1
        print(outut)
hist([1,2,4,1])