class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        
        """
        num1=''.join([str(ord(i)-97) for i in firstWord])
        num2=''.join([str(ord(i)-97) for i in secondWord])
        num3=''.join([str(ord(i)-97) for i in targetWord])
        return int(num1)+int(num2)==int(num3)
    