from typing import List


# O(n ^ n)
def bubbleSort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array



# Slightly more efficient than bubbleSort
# O(n ^ n)
def selectionSort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        min = i             # assume index i is the min value
        for j in range(i+1, len(array)):
            if array[min] > array[j]:     # turn out array[min] is not the mininum
                min = j                   # so change min to j
        array[i], array[min] = array[min], array[i]   # then swap the position array[i] with array[min]
    return array



array = [9,8,7,6,5,4,3,2,1]
print(f'Original Array: {array}')
print(f'Bubble sorted Array: {bubbleSort(array)}')
print("")

array = [9,8,7,6,5,4,3,2,1]
print(f'Original Array: {array}')
print(f'Selection sorted Array: {selectionSort(array)}')
print("")