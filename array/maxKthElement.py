import heapq
'''
O (n log n)

Parent node representation
    array[(i -1) / 2] 
Left child node representation
    array[(2 * i) + 1]
Right child node representation
    array[(2 * i) + 1]

In Python, by default the heap is MinHeap there is no MaxHeap
So, to find kthMaxElement, we need to:
    * modify all element to -negative value
    * so that when creating heap using heapify
    * we reverse it, the max value becomes the min val
    * when we heappop it, we multiply it with -1 to get the actual value
'''

def findKthMaxElement(myList, kth):
    myList = [i * -1 for i in myList]
    heapq.heapify(myList)
    print(myList)
    for i in range(kth):
        kthMax = heapq.heappop(myList)

    return kthMax * -1


def findKthMaxElement2(myList, kth):
    # Another way is by sorting the list first
    # then pick the element from the right

    myList.sort()
    return myList[-2]



myList = [15, 7, 9, 4, 13]
print(findKthMaxElement(myList, 2))
'''
Orig myList = [15, 7, 9, 4, 13]
Updated myList = [-15, -7, -9, -4, -13]
heapify = [-15, -13, -9, -4, -7]
kth = 2 -> heappop 2 times -> get -13
return -13 * -1 = 13

Output: 13
'''
print(findKthMaxElement2(myList, 2))
