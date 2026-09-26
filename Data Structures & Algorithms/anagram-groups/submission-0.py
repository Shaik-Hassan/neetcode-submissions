class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        res = {}
        
        for s in strs:
            t = "".join(sorted(s))
            if t not in res:
                res[t] = []
            res[t].append(s)

        final = []
        for m in res:
            final.append(res[m])
        
        return final

            
            

            
        
        print(res)

