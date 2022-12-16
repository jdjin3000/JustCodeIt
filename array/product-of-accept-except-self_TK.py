class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = 1
        left = 1
        result = []
        for i in range(len(nums)):
            result.append(right)
            right *= nums[i]


        for i in range(len(nums) - 1, 0, -1):
            left *= nums[i]
            result[i-1] *= left
        
        return result