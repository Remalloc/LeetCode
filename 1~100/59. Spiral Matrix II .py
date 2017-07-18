class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        column=[]
        for i in range(n):
            row = []
            for j in range(n):
                row.append(-1)
            column.append(row)
        num=1
        judge=1
        x,y=0,0
        while num<=n*n:
            column[y][x] = num
            if judge==1:
                if x+1==n or column[y][x+1]!=-1:
                    y+=1
                    judge=2
                else:
                    x+=1
            elif judge==2:
                if y+1==n or column[y+1][x]!=-1:
                    x-=1
                    judge=3
                else:
                    y+=1
            elif judge==3:
                if x-1==0 or column[y][x-1]!=-1:
                    y-=1
                    judge=4
                else:
                    x-=1
            elif judge==4:
                if y-1==0 or column[y-1][x]!=-1:
                    x+=1
                    judge=1
                else:
                    y-=1
            num+=1
        return column