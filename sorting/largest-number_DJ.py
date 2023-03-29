class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mergeSort(l1, l2):
            answer = []
            while l1 and l2:
                n1, n2 = l1[0], l2[0]

                if str(n1) + str(n2) < str(n2) + str(n1):
                    answer.append(l2.pop(0))
                else:
                    answer.append(l1.pop(0))
            
            if l1:
                answer.extend(l1)
            elif l2:
                answer.extend(l2)

            return answer

        def divide(nums):
            if len(nums) <= 1:
                return nums
            
            l1 = divide(nums[:len(nums) // 2])
            l2 = divide(nums[len(nums) // 2:])

            return mergeSort(l1, l2)

        return str(int(''.join(map(str, divide(nums)))))