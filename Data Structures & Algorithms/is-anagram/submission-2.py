class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = "".join(filter(str.isalpha, s))
        t = "".join(filter(str.isalpha, t))

        if len(s) != len(t):
            return False

        mapS = {}
        for ch in s:
            mapS[ch] = 1 + mapS.get(ch,0)

        mapT = {}
        for ch in t:
            mapT[ch] = 1 + mapT.get(ch,0)


        return mapS==mapT        


        
        