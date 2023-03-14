class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]

        for num in nums[:-1]:
            left.append(left[-1] * num)
        
        for num in nums[::-1][:-1]:
            right.append(right[-1] * num)
        
        return [l*r for l, r in zip(left, right[::-1])]