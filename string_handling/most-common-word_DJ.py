class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz" + " "
        paragraph_lower = "".join([_ if _ in alphabet else ' ' for _ in paragraph.lower()])
        
        counts = dict()
        for word in paragraph_lower.split():
            if word in banned:
                continue
            if not word in counts.keys():
                counts[word] = 0
            counts[word] += 1
        
        return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0]