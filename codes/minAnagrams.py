def number_needed(a, b):
    charMap = {}
    for c in a:
        if c in charMap:
            charMap[c] = charMap[c]+1
        else:
            charMap[c] = 1
    deletions = 0
    
    for c in b:
        if c in charMap:
            if charMap[c] > 0:
                charMap[c] = charMap[c]-1
            else:
                deletions = deletions+1
        else:
            deletions = deletions+1

    for c in charMap:
        if charMap[c] > 0:
            deletions = deletions + charMap[c]
    return deletions 
