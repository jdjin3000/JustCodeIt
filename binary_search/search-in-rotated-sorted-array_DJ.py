class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # pivot = nums.index(min(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # distnict values라 같은 경우는 없음.
            if nums[mid] > nums[right]: # mid와 right 사이에 pivot이 존재하는 경우.
                left = mid + 1
            else: # mid와 right 사이에 pivot이 존재하지 않는 경우.
                right = mid

        pivot = left

        def binary_search(start, end):
            if start <= end:
                mid = (start + end) // 2
                mid_pivot = (mid + pivot) % len(nums)
                
                if nums[mid_pivot] < target:
                    return binary_search(mid + 1, end)
                elif nums[mid_pivot] > target:
                    return binary_search(start, mid - 1)
                else:
                    return mid_pivot
            
            return -1
        
        return binary_search(0, len(nums))