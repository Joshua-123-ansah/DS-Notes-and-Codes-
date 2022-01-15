
#THIS IMPLEMENTATION IS THE TOP-DOWN APPRAOCH 
class Solution:
  #THIS APPROACH DOES NOT HAVBE A BETTER TIME COMPLEXITY. TO OPTIMIZED IT WE WILL USE MEMOIZATION
    def climbStairs(self, n: int) -> int:
        def dp(i): 
            """A function that returns the answer to the problem for a given state."""
            # Base cases: when i is less than 3 there are i ways to reach the ith stair.
            if i <= 2: 
                return i
            
            # If i is not a base case, then use the recurrence relation.
            return dp(i - 1) + dp(i - 2)
        
        return dp(n)


#THIS IS THE OPTIMIZED CODE  
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 2: 
                return i
            if i not in memo:
                # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
                # store the result inside a hashmap to refer to in the future.
                memo[i] = dp(i - 1) + dp(i - 2)
            
            return memo[i]
        
        memo = {}
        return dp(n)

#THIS IS THE IMPLEMENTATION FOR THE BUTTOM-UP APPRAOCH 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
            
        # An array that represents the answer to the problem for a given state
        dp = [0] * (n + 1)
        dp[1] = 1 # Base cases
        dp[2] = 2 # Base cases
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # Recurrence relation

        return dp[n]