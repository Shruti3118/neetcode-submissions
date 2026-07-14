class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hm = {}
        for i in range(len(position)):
            hm[position[i]] = speed[i]
        position.sort(reverse = True)
        stack = []
        for i in range(len(position)):
            dist = target - position[i] 
            time = dist / hm[position[i]]
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)







