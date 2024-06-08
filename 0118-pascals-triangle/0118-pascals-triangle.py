class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1],[1,1]]
        if numRows<3:
            return triangle[:numRows]
        for n in range(3,numRows+1):
            newRow=[triangle[-1][0]]
            for i in range(1,len(triangle[-1])):
                newRow.append(triangle[-1][i]+triangle[-1][i-1])
            newRow.append(triangle[-1][-1])
            triangle.append(newRow)
        return triangle 

        