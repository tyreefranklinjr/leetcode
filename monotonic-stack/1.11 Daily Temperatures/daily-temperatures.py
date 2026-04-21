class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Declare the essential variables
        res = [0] * len(temperatures)
        stack = []

        # For loop to run each temperature
        for i , temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index
                
            stack.append(i)
        
        return res
