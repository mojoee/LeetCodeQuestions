from numpy import equal


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        local_max=0
        global_max=float('-inf')
        for i in range(len(nums)):
            local_max=max(nums[i], nums[i]+local_max)
            if local_max>global_max:
                global_max=local_max
        return global_max

if __name__=="__main__":
    solution=Solution()
    a=solution.maxSubArray([-1])
    print(a)
    b=solution.maxSubArray([5,4,-1,7,8])
    print(b)
    assert b==23
