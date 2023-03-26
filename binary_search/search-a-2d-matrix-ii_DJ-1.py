class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        queue = [(len(matrix) // 2, len(matrix[0]) // 2)]
        visited = []

        while queue:
            x, y = queue.pop(0)

            if (x, y) in visited:
                continue
            
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if matrix[x][y] > target:
                    queue.append((x - 1, y))
                    queue.append((x, y - 1))
                elif matrix[x][y] < target:
                    queue.append((x + 1, y))
                    queue.append((x, y + 1))
                else:
                    return True
                
                visited.append((x, y))

        
        return False