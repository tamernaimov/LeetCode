class Solution():
    def lengthOfLastWord(self,s):
        words = s.strip().split(" ")
        word = words[len(words) - 1]
        counter = 0
        for char in word:
            counter += 1
        return counter
