class MySolution:
    # use bruteForce for simplicity
    # time complexity = O(nxn)
    def twoSum_bruteForce(self, nums, target):
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append([nums[i],nums[j]])
        return result


    # we optimize it by finding its compliment value
    # time complexity = O(n)
    def twoSum_optimized(self, nums, target):
        result = []
        map = dict()
        for num in nums:
            compliment = target - num
            if num in map:
                result.append([map[num], num])
            else:
                map[compliment] = num
        return result


    ## if nums are in sorted order
    ## we can use binary search approach to optimize the solution
    def twoSum_bruteForce2(self, nums, target):  ## O(nxn)
        mid = len(nums) // 2
        result = []
        for i in range(mid):
            compliment = target - nums[i]
            if compliment >= nums[mid]:
                start = mid
                end = len(nums)
            else:
                start = 0
                end = mid
            for j in range(start, end):
                if nums[i] + nums[j] == target:
                    result.append([nums[i],nums[j]])
        return result


if __name__ == '__main__':
    ms = MySolution()
    nums = [1,5,2,4,3]
    target = 6
    print(ms.twoSum_bruteForce(nums, target))
    print(ms.twoSum_optimized(nums, target))

    nums = [1, 2, 50, 55, 56, 57]
    target = 57
    print(ms.twoSum_bruteForce2(nums, target))
