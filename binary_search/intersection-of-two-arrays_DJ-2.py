class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(start, end):
            if start <= end:
                mid = (start + end) // 2

                if nums2[mid] > target:
                    return binary_search(start, mid - 1)
                elif nums2[mid] < target:
                    return binary_search(mid + 1, end)
                else:
                    return mid

        answer = set()
        nums2.sort()
        
        # 한 set은 순차적으로 탐색하고, 다른쪽은 정렬해서 이진 검색으로 값을 찾기.
        for target in nums1:
            if binary_search(0, len(nums2) - 1) is not None:
                answer.add(target)
        
        return answer