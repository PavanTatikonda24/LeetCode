class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        for word in reversed(s.split()):
            result+=word
            result+=" "
        final=result.strip()
        return final


