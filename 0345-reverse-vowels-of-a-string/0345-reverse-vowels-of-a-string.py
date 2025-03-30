class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v={"a","e","i","o","u","A","E","I","O","U"}
        vowels=[]
        for i in s:
            if i in v:
                vowels.append(i)
        result=""
        for a in s:
            if a in v:
                result+=vowels[-1]
                vowels.pop()
            else:
                result+=a
        return result

