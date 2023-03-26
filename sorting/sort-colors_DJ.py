class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quickSort(start, end):
            if start >= end:
                return
            
            mid = partition(start, end)
            quickSort(start, mid - 1)
            quickSort(mid, end)
        
        def partition(start, end):
            pivot = nums[(start + end) // 2] # 중간 pivot

            while start <= end:
                while nums[start] < pivot:
                    start += 1
                while nums[end] > pivot:
                    end -= 1
                
                if start <= end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start, end = start + 1, end - 1

            return start

        quickSort(0, len(nums) - 1)
                    

            