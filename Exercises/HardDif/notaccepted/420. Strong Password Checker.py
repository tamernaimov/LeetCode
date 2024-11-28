import re

def strongPasswordChecker(password):
    steps = 0
    length = len(password)
    print(length)
    check = False
    check2 = False
    contains_digit = bool(re.search(r'\d',password))

    if not contains_digit:
        password += "0"
        steps +=1
        length +=1

    while length < 6:
        for i in range(len(password)-2):
            if password[i] == password[i+1] == password[i+2]:
                if password[i] == password[i].upper():
                    password = password.replace(password[i],password[i].lower(),1)
                elif password[i] == password[i].lower():
                    password = password.replace(password[i],password[i].upper(),1)
                print(password)
                steps +=1

        #repeat that again
        for i in range(len(password)-2):
            if password[i] == password[i+1] == password[i+2]:
                if password[i] == password[i].upper():
                    password = password.replace(password[i],password[i].lower(),1)
                elif password[i] == password[i].lower():
                    password = password.replace(password[i],password[i].upper(),1)
                steps +=1

        length +=1
        steps+=1




    while length > 20:
        if password == password.lower() and not check :
            check = True
            steps +=1
            length +=1
        if password == password.upper() and not check2 :
            check2 = True
            steps +=1
            length +=1
        for i in range(len(password)-2):
            if password[i] == password[i+1] == password[i+2]:
                if password[i] == password[i].upper():
                    password = password.replace(password[i],password[i].lower(),1)
                elif password[i] == password[i].lower():
                    password = password.replace(password[i],password[i].upper(),1)
                steps +=1

        #repeat that again
        for i in range(len(password)-2):
            if password[i] == password[i+1] == password[i+2]:
                if password[i] == password[i].upper():
                    password = password.replace(password[i],password[i].lower(),1)
                elif password[i] == password[i].lower():
                    password = password.replace(password[i],password[i].upper(),1)
                steps +=1
        length -= 1

        if check:
            steps +=1
            continue
        if check2:
            steps +=1
            continue
        steps+=1

    return steps
print(strongPasswordChecker("aaa"))