a=[1,2,3,2,3,2,3]

def Mode(a):
    w={}
    for x in a:
        if(x in w.keys()):
            w[x]+=1
        else :
            w[x]=1
    q=1
    r=[]
    for y in w:
        if (w[y]>q):
            r=[y]
            q=w[y]
        elif (w[y]==q):
            r.append(y)
    if (len(r)==len(w.keys())):
        r=[]
    print(r)

Mode(a)