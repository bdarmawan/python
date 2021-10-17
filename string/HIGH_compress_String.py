from typing import List

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

        if (count == 1):                    #No need to print count if cur is 1 occurence
            continue                        #For example:   a or b or c only

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
