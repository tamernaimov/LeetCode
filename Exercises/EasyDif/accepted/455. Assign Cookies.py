def findContentChildren(g,s):
    counter = 0
    g.sort()
    s.sort()
    gc = 0
    sc = 0

    while gc< len(g) and sc < len(s):
        if g[gc] <= s[sc]:
            counter+=1
            gc+=1
        sc+=1

    return counter

print(findContentChildren([1,2,1,1,1,1,4],[1,2,3,7,8]))

