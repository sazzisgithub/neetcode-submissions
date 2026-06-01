class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq={}
        if len(s)!=len(t):
            return False

        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for j in t:
            if j not in freq:
                return False
            freq[j]-=1

            if freq[j]<0:
                return False
        return True