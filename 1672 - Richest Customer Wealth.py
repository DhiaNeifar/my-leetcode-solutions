class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        number_customers, number_banks = len(accounts), len(accounts[0])
        max_wealth = 0
        for customer_index in range(number_customers):
            customer_wealth = sum(accounts[customer_index])
            max_wealth = max(customer_wealth, max_wealth)
        return max_wealth