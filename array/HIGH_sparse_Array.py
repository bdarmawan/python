import os


def matchingStrings(strings, queries):
    # Write your code here
    strMap = {}
    qMap = {}
    for string in strings:
        if string in strMap:
            strMap[string] += 1
        else:
            strMap[string] = 1
    print(strMap)

    for query in queries:
        if query in strMap:
            qMap[query] = strMap[query]
        else:
            qMap[query] = 0
    return qMap.values()


if __name__ == '__main__':

    strings = ['aba', 'baba', 'aba', 'xzxb']
    queries= ['aba', 'xzxb', 'ab']

    res = matchingStrings(strings, queries)

    print(' '.join(map(str, res)))         #OUTPUT: 2, 1, 0
