def wordBreak(s,wordDict):
   word = ""
   i = 0
   length = 0
   bc = False
   while word !=s:
       if wordDict[i] == s[length:length + len(wordDict[i])]:
           word += wordDict[i]
           length += len(wordDict[i])
           i = 0

       else:
           if i < len(wordDict) - 1:
               i +=1
           else:
               return False

       if word == s:
           return True


   if bc:
       return False
   return True


print(wordBreak("ptukamaina",["pteuka","maina"]))