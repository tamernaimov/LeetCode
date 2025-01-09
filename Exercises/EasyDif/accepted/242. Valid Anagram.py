from collections import deque


def isAnagram(s,t):
    sorted_s = ''.join(sorted(s))
    sorted_t = ''.join(sorted(t))
    if sorted_s == sorted_t:
        return True
    else:
        return False



def isAnagram2(s,t):
    st = deque()

    if len(s) >= len(t):
        for i in range (len(s)):
            st.append(s[i])

        for i in range (len(t)):
            if t[i] in st:
                st.remove(t[i])
    else:
        for i in range(len(t)):
            st.append(t[i])

        for i in range(len(s)):
            if s[i] in st:
                st.remove(s[i])
    if st:
        return False
    return True


print(isAnagram2("anagram","nagaram")) #both solutions work