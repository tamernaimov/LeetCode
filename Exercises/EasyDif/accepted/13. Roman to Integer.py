def romanToInt(s):
    num_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,  "CD": 400,
            "C": 100,  "XC":90 ,
            "L": 50 ,   "XL": 40,
            "X": 10,   "IX": 9,
            "V": 5,    "IV": 4,
            "I":1
        }
    res = 0
    check = False
    lastCheck = False


    for i in range (len(s)-1):

        if check:
            check = False
            continue

        if s[i] + s[i+1] in num_map:
            res += num_map[s[i]+s[i+1]]
            check = True
            if i == len(s)-2:
                lastCheck = True

        else:
            res += num_map[s[i]]
            if i == len(s)-1:
                lastCheck = True

    if not lastCheck:
        res += num_map[s[-1]]

    return res

print(romanToInt("LVIII"))
