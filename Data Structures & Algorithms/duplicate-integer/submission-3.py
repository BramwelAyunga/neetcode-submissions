class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = []
        for num in nums:
            if num in n:
                return True
            n.append(num)
        return False
            
            
    


