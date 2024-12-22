def merge(intervals):
    length = len(intervals) - 1
    for i in range(length):
        if length == 1:
            if intervals[0][1] >= intervals[1][0]:
                intervals[0][1] = intervals[1][1]
                del intervals[1]
                return intervals


        if i >= length: #2
            return intervals

        if intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = intervals[i+1][1]
            del intervals[i+1]
            length -=1

    return intervals

print(merge([[1,4],[0,5]]))