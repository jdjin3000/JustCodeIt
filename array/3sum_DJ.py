class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        for i, n in enumerate(nums):
            left, right = i+1, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < -n:
                    left +=1
                elif nums[left] + nums[right] > -n:
                    right -= 1
                else: # if n + nums[left] + nums[right] == 0
                    answer.add((n, nums[left], nums[right]))

                    left += 1 # right -=1 이어도 상관 없음. 단지 다음 계산을 위한 방법.
        
        return map(list, list(answer))
