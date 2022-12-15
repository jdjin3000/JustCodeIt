class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word] += [word]
            
        for d in dic.values():
            result.append(d)

        return result