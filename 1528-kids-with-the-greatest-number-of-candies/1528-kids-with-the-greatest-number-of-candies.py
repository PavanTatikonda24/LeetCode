class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        for c in candies:
            a=c+extraCandies
            if a>=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

        