class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
            curr=i
            is_dividing=True
            while curr:
                rem=curr%10
                if rem==0 or i%rem!=0:
                    is_dividing=False
                    break
                curr=curr//10
            if is_dividing:
                result.append(i)
        return result


        