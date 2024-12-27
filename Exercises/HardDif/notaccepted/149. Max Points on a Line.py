def maxPoints(points):
    max_counter = 0
    new_points = [[]]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[j][0] < points[i][0]:
                points[j], points[i] = points[i], points[j]

    print(points)


    for i in range (len(points)):
        counter = 0
        for j in range (i,len(points) -1):

            if points[j][0] -1 == points[j+1][0]:
                if points[j][1] + 1 == points[j+1][1]:
                    counter+=1


            if points[j][0] +1 == points[j+1][0]:
                if points[j][1] -1 == points[j+1][1]:
                    counter+=1


            if points[j][0] -1 == points[j+1][0]:
                if points[j][1] -1 == points[j+1][1]:
                    counter+=1


            if points[j][0] +1 == points[j+1][0]:
                if points[j][1] +1 == points[j+1][1]:
                    print(":asd")
                    counter+=1

            #equal

            if points[j][0] == points[j+1][0]:
                if points[j][1] +1 == points[j+1][1]:
                    counter+=1

            if points[j][0] == points[j+1][0]:
                if points[j][1] -1 == points[j+1][1]:
                    counter+=1


        if counter> max_counter:
            max_counter = counter

    return max_counter +1

print(maxPoints([[5,1],[4,2],[3,2],[2,3],[1,2],[1,4]]))