def Towers(n=4,a=[],b=[],c=[]):
    if n > 0:
        Towers(n-1,a,b,c)
        c.append(b.pop())
        Towers(n-1,b,c,a)
Towers(a=[z+1 for z in range(4)])
