def sortirane(imena):
    allTeams = []
    for i in range (len(imena)):
        for j in range (i+1,len(imena)):
            allTeams.append([imena[i],imena[j]])
    return allTeams

print(sortirane(["Tamer","Sisko","Eren","Kristiqno","Djem","Qskan"]))