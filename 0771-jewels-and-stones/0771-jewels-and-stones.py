class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # return sum(s in J for s in S)
        sc = collections.Counter(stones)
        count = 0 
        for j in jewels:
            count += sc[j]
        return count 