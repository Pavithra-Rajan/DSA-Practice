class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
       
        max_wealth=0
        for i in range(len(accounts)):
            if sum(accounts[i])>max_wealth:
                max_wealth=sum(accounts[i])
        
        return max_wealth
            