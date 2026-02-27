class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        for x,y in points:
            dist = math.sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(heap,(dist,x,y))

        result = []
        for _ in range(k):
            (dist,x,y) = heapq.heappop(heap)
            result.append([x,y])
        return result 
