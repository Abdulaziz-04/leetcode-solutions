class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        minBlocks=k
        total_blocks=0
        for r in range(len(blocks)):
            if blocks[r]=='B':
                total_blocks+=1
            if r-l+1>k:
                if blocks[l]=='B':
                    total_blocks-=1
                l+=1
            if r-l+1==k:
                minBlocks=min(minBlocks,k-total_blocks)
        return minBlocks


        