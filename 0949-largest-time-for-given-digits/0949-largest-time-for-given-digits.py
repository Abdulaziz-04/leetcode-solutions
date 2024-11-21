class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result=[]
        def permute(perms,arr,pick):
            if len(perms)==len(arr):
                result.append(perms.copy())
                return
            for i in range(len(arr)):
                if not pick[i]:
                    perms.append(arr[i])
                    pick[i]=True
                    permute(perms,arr,pick)
                    perms.pop()
                    pick[i]=False
        permute([],arr,[False]*len(arr))
        result.sort(reverse=True)
        for time in result:
            h1,h2,m1,m2=time
            if h1*10+h2<24 and m1*10+m2<60:
                return f'{h1}{h2}:{m1}{m2}'
        return ""

        