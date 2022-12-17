class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in num_idx.keys() and i != num_idx[target - num]:
                return [i, num_idx[target - num]]