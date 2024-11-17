
def longestCommonPrefix(strs):
    if not strs:
        print('""')  # In case the input is empty, print empty string
        return ""

    # Start with the first word as the initial prefix
    prefix = strs[0]

    for i in range(1, len(strs)):
        # Compare the prefix with the current word
        while not strs[i].startswith(prefix):
            # Shorten the prefix by one character at a time
            prefix = prefix[:-1]
            if not prefix:
                print('""')  # If no common prefix is found, print empty string
                return ""

    return prefix
