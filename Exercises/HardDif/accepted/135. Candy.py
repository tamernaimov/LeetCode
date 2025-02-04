def candy(ratings):
    n = len(ratings)
    uni = [1] * n  # Start with 1 candy for each child

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            uni[i] = uni[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            uni[i] = max(uni[i], uni[i + 1] + 1)

    return sum(uni)

print(candy([1,2,3,2,1,7,1,2,3,6,1,2,3,45,7,8,9,3,2,3,4]))



def candy2(ratings):

    uni = [1] * len(ratings)

    if ratings[0] > ratings[1]:
        uni[0] += 1



    print(uni)
    for i in range (1,len(ratings)-1):
        if ratings[i-1] < ratings[i]:
            uni[i] = uni[i-1] + 1
        elif ratings[i+1]  < ratings[i]:
            uni[i] = uni[i+1] +1

    if ratings[-1] > ratings[-2]:
        uni[-1] = uni[-2] +1
    elif ratings[-2] > ratings[-1]:
        uni[-2] = 2



    return sum(uni)



#print(candy2([1,2,87,87,87,2,1]))
 #45