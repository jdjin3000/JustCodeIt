import re 
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        cnt = Counter()
        paragraph = paragraph.lower()
        paragraph = re.sub('[^0-9a-z\s]', ' ', paragraph)
        for word in paragraph.split():
            if (word not in banned):
                cnt[word] += 1

        return cnt.most_common()[0][0]