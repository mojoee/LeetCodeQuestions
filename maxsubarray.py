from numpy import equal


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum_list=[]
        for i in range(len(nums)):
            subsum=[]
            notattached=[]
            for num in nums[i:]:
                notattached.append(num)
                if sum(notattached)>0:
                    subsum.extend(notattached)
                    notattached=[]
            if sum(subsum)>sum(max_sum_list):
                max_sum_list=subsum
        return max_sum_list

if __name__=="__main__":
    solution=Solution()
    a=solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(a)
    assert a==[4,-1,2,1]
    b=solution.maxSubArray([5,4,-1,7,8])
    print(b)
    assert sum(b)==23
