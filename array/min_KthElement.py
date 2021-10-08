import heapq
'''
A heapsort can be implemented by pushing all values onto a heap and 
then popping off the smallest values one at a time
'''
from typing import List

def findKthMin(a: List[int], k: int) -> int:
    if len(a) == 0:  return 0
    if k > len(a):
        maxSize = len(a)
        return "k is too big.  Should be <= " + str(maxSize)
    heapq.heapify(a)
    for _ in range(k):
        small = heapq.heappop(a)
    return small


def findKthMin2(a: List[int], k: int) -> int:
    b = sorted(a, reverse = True)
    print(b)
    return b[-k]



if __name__ == "__main__":
    a = [10, 5, 1, 4, 2]
    print(findKthMin(a, 2))     # OUTPUT: 2
    a = [10, 5, 1, 4, 2]
    print(findKthMin(a, 3))     # OUTPUT: 4
    a = []
    print(findKthMin(a, 3))     # OUTPUT: 0
    a = [10, 5, 1, 4, 2]
    print(findKthMin(a, 9))     # OUTPUT: k is too big.  Should be <= 5

    a = [10, 5, 1, 4, 2]
    print(findKthMin2(a, 3))     # OUTPUT: 4
