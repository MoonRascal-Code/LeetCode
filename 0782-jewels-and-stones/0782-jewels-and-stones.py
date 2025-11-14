class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0 
        splits = collections.Counter(stones)
        for char in jewels:
            if char in splits:
                c += splits[char]
        return c 