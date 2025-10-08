def getidx(list,idx):
    try:
        res=list[idx]
    except IndexError:
        print("Index out of bounds")
    else: print(res)

getidx([4,3,2,10] , 5)