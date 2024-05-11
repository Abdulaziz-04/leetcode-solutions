class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            l,r=0,len(row)-1
            while l<r:
                row[l],row[r]=int(not row[r]), int(not row[l])
                l+=1
                r-=1
            if l==r:
                row[l]=int(not row[l])

        return image
        