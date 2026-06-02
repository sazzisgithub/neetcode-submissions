class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        
        for k,v in freq.items():
            if v==1:
                return k