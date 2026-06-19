class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for s in sentences:
            count=len(s.split())
            if count>maxi:
                maxi=count
        return maxi        