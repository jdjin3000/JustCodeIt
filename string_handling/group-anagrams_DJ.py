class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [("".join(sorted(list(s))), s) for s in strs]
        results = dict()

        for letters, s in strs:
            if not letters in results.keys():
                results[letters] = list()
            results[letters].append(s)
        
        return results.values()