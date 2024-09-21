class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_count={0:0}
        for row in wall:
            total=0
            for brick in row[:-1]:
                total+=brick
                gap_count[total]=1+gap_count.get(total,0)
        return len(wall)-max(gap_count.values())

        