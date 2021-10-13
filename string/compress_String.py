from typing import List

'''
        aaabbcccc
    i   ^  ^ ^
    j   ^^^^^^^^^
'''
def compress(chars: List[str]) -> int:
    i, j = 0, 0
    count = 0
    stored = ""
    res = []

    if len(chars) == 1 and chars[0] == 'a':
        return 1

    while i < len(chars):
        stored = chars[i]
        while j < len(chars) and chars[j] == chars[i]:
            j += 1
            count = j - i
        res.append(stored)
        res.append(str(count))
        # chars[i] = stored
        # chars[i+1] = str(count)
        i = j

    return res
    # return chars





def compressWorkOne(chars: List[str]) -> int:
    indexRes, i = 0, 0
    while i < len(chars):
        cur = chars[i]
        count = 1
        while (i+1 < len(chars)  and  chars[i+1] == cur):
            i += 1
            count += 1
        chars[indexRes] = cur               #Ths is for storing the character

        indexRes += 1
        i += 1

        if (count == 1):
            continue

        for c in str(count):
            chars[indexRes] = c
            indexRes += 1                   #Ths is for storing the count

    print(chars)
    return indexRes


string = ["a","a","b","b","c","c","c"]
print(compressWorkOne(string))      #OUPUT: ['a', '2', 'b', '2', 'c', '3', 'c']
                                    #       6

string = ["a"]
print(compressWorkOne(string))      #OUTPUT: ['a']
                                    #       1

string = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compressWorkOne(string))      #OUTPUT: ['a', 'b', '1', '2', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
                                    # 4
