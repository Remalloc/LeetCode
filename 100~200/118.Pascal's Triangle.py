class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        row=0
        while row<numRows:
            temp=[1]
            if row!=0:
                for i in range(len(result[row-1])):
                    msum=result[row-1][i]
                    if i+1!=len(result[row-1]):
                        msum+=result[row-1][i+1]
                    temp.append(msum)
            result.append(temp)
            row+=1
        return result