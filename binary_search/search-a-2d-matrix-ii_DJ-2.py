class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1

        # matrix가 왼쪽에서 오른쪽, 위에서 아래로오름차순으로 정렬되어 있기 때문에,
        # 시작을 맨위 오른쪽에서 출발하여
        # 작으면 왼쪽, 크면 아래로 이동하면 어렵지 않게 도달 가능함.
        while row < len(matrix) and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        
        return False