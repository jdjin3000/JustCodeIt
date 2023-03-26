class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        answer = []
        for interval in intervals:
            if not answer:
                answer.append(interval)
                continue

            prev_s, prev_e = answer[-1]
            s, e = interval
            
            if (prev_s <= s and prev_e >= s) or (prev_s <= e and prev_e >= e):
                prev_s, prev_e = answer.pop()
                new_s, new_e = s if s <= prev_s else prev_s, e if e >= prev_e else prev_e
                answer.append([new_s, new_e])
            else:
                answer.append(interval)
        
        return answer

            