class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')]*n

        dist[src] = 0

        for count in range(k+1):
            temp_dist = dist[:]
            
            for u, v, price in flights:  
                if temp_dist[v] > dist[u] + price:
                    temp_dist[v] = dist[u] + price
            
            dist = temp_dist[:]
            
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]