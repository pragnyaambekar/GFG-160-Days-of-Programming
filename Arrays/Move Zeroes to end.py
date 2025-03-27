#https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

class Solution:
    def pushZerosToEnd(self,nums):
        nonzero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonzero],nums[i] = nums[i],nums[nonzero]
                nonzero +=1
        return nums

