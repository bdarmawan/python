from typing import List

def findPivot_in_RotatedArray(nums: List) -> int:
    n = len(nums)
    left = 0
    right = n    # we don't use n - 1 here b/c we don't access nums[right]
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] > nums[mid + 1]:    # check if mid el is > the next one
            return mid + 1               # if yes, then we get the pivot there
        elif nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_element_in_rotated_array(nums: List, target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1   # we use n - 1 b/c we want to access nums[right]
    while left <= right:                    # [5, 6, 7, 8, 0, 1, 2, 3, 4]
        mid = (right + left) // 2           #  l          mid          r
        if target == nums[mid]:
            return mid
        elif nums[left] <= nums[mid]:                          # [5, 6, 7, 8, 0
            if nums[left] <= target <= nums[mid]:              #  l          mid
                right = mid - 1                                #  <-- target -->
            else:
                left = mid + 1
        else:                                                  # 0, 1, 2, 3, 4]
            if nums[mid] <= target <= nums[right]:             # mid         r
                left = mid + 1                                 # <-- target -->
            else:
                right = mid - 1
    return -1


nums = [5, 6, 7, 8, 0, 1, 2, 3, 4]
print(f"Pivot's position: {findPivot_in_RotatedArray(nums)}, element: {nums[findPivot_in_RotatedArray(nums)]}")
nums = [5, 6, 7, 8, 0, 1, 2, 3]
print(f"Pivot's position: {findPivot_in_RotatedArray(nums)}, element: {nums[findPivot_in_RotatedArray(nums)]}")
nums = [5, 6, 7, 8, 9, 10, 0, 1, 2, 3]
print(f"Pivot's position: {findPivot_in_RotatedArray(nums)}, element: {nums[findPivot_in_RotatedArray(nums)]}")
print()
nums = [5, 6, 7, 8, 0, 1, 2, 3, 4]
print(f"Search for 7: {search_element_in_rotated_array(nums, 7)}th element")
nums = [5, 6, 7, 8, 0, 1, 2, 3]
print(f"Search for 7: {search_element_in_rotated_array(nums, 7)}th element")
nums = [5, 6, 7, 8, 9, 10, 0, 1, 2, 3]
print(f"Search for 2: {search_element_in_rotated_array(nums, 2)}th element")

"""
Pivot's position: 4, element: 0
Pivot's position: 4, element: 0
Pivot's position: 6, element: 0

Search for 7: 2th element
Search for 7: 2th element
Search for 2: 8th element
"""