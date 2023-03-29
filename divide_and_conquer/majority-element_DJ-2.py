class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return a if nums.count(a) > half else b 
        # 부등호가 >= 여선 안된다. len(nums) // 2은 len(nums)가 홀수일 때, 과반보다 작게 측정되기 때문이다.