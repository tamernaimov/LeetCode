def ex2(word):
    unique_chars = []
    for i in range (len(word)-1):
       if word[i].isdigit() and word[i+1].isdigit():
           continue
       elif word[i].isdigit() and not word[i+1].isdigit():
           unique_chars.append(word[i+1])
           i+=1
       else:
           unique_chars.append(word[i])
    word = ""
    for i in range(len(unique_chars)):
        word += unique_chars[i]

    return word
print(ex2("bla3vf3223312")) #blavf