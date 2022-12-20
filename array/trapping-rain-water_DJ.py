class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        left_wall, right_wall = height[left], height[right]

        while left < right:
            # left, right가 이동하면서 벽의 높이가 낮아질 때 받칠 수 있는 벽을 계산하기 위해 max 사용
            left_wall, right_wall = max(left_wall, height[left]), max(right_wall, height[right])

            if left_wall <= right_wall:
                water += left_wall - height[left]
                left += 1
            else:
                water += right_wall - height[right]
                right -= 1
        
        return water