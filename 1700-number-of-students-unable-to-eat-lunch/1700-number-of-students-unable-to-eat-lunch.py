from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=Counter(students)
        res=len(students)
        for s in sandwiches:
            # If there exists a student willing to eat that sandwich
            if cnt[s]>0:
                res-=1
                cnt[s]-=1
            else:
                return res
        return res

        