class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,total,result=0,0,0
        fruit_map=defaultdict(int)
        for r in range(len(fruits)):
            fruit_map[fruits[r]]+=1
            total+=1
            if len(fruit_map)>2:
                curr_fruit=fruits[l]
                fruit_map[curr_fruit]-=1
                total-=1
                l+=1
                if not fruit_map[curr_fruit]:
                    fruit_map.pop(curr_fruit)
            result=max(result,total)
        return result
            

        