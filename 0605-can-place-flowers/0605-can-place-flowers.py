class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        chances=0
        l=len(flowerbed)
        for i in range(l):
            if flowerbed[i]==0:
                before=(i==0) or flowerbed[i-1]==0
                after=(i==l-1) or flowerbed[i+1]==0
                if before and after:
                    flowerbed[i]=1
                    chances+=1
        if chances>=n:
            return True
        else:
            return False



        