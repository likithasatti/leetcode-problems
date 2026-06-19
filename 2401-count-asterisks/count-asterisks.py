class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        inside=False
        for ch in s:
            if ch =='|':
                inside=not inside
            elif ch=='*' and not inside:
                c+=1
        return c            