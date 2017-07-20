class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag=len(digits)-1
        plus_num=1
        next_num =0
        while flag>=0:
            if flag+1==len(digits):
                next_num=digits[flag]+plus_num
                digits[flag]=next_num%10
                next_num=next_num//10
            else:
                if next_num!=0:
                    next_num+=digits[flag]
                    digits[flag]=next_num%10
                    next_num=next_num//10
            flag-=1
        if next_num!=0:
            digits.insert(0,next_num)
        return digits
