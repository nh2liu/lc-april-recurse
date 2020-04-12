class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        h = [-x for x in stones]
        heapq.heapify(h)
        
        while len(h) >= 2:
            large = heapq.heappop(h)
            small = heapq.heappop(h)
            heapq.heappush(h, large - small)
        return -h[0]
