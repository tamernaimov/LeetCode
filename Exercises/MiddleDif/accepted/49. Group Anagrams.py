def groupAnagrams(strs):
    sorted_strs = []
    for i in range(len(strs)):
        sorted_str = ''.join(sorted(strs[i]))
        sorted_strs.append(sorted_str)
    unique_list = list(dict.fromkeys(sorted_strs))

    res = []
    hashmap = {}
    for i in range(len(unique_list)):
        hashmap[unique_list[i]] = []

    for str in strs:
        sorted_str = ''.join(sorted(str))
        if sorted_str in hashmap:
            hashmap[sorted_str].append(str)

    for str in hashmap:
        res.append(hashmap[str])

    return res
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))