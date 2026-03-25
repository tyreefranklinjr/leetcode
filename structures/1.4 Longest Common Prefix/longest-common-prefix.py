class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strs.sort()
        beginning = strs[0]
        final = strs[-1]
        index = 0
        output = ""

        for x in beginning:
            if x == final[index]:
                output += x
            else:
                break
            index += 1
            
        return output
