class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for num in nums]
        postfix = [1 for num in nums]
        res = [1 for num in nums]

        for i in range(len(prefix)):
            if i == 0:
                continue
            prefix[i] *= prefix[i - 1] * nums[i - 1]
        for i in range(len(postfix) - 1, -1, -1):
            if i == len(postfix) - 1:
                continue
            postfix[i] *= postfix[i + 1] * nums[i + 1]
        for i in range(len(res)):
            res[i] = prefix[i] * postfix[i]
        
        return res

        
        
            
