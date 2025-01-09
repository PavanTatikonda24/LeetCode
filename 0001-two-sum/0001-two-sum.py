class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for a,b in enumerate(nums):
            c=target-b
            if c in dict:
                return(dict[c],a)
            dict[b]=a
                    