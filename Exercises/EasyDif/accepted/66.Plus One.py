class Solution():
    def plusOne(self,digits):
        strNum = ""
        for i in range(len(digits)):
            strNum += str(digits[i])
        intNum = int(strNum)
        intNum += 1
        list = []  # the returning
        listSize = len(str(intNum))  # size
        strNum = str(intNum)
        print(listSize)
        for i in range(listSize):
            list.appendint((strNum[i]))
        return list
