from typing import List


# you have prices of stock in each day int array [2, 1, 5, 6, 7, 3, 4].
# Each position represents a day. first day = prices[0] = 2, second day = prices[1] = 1 etc...
# your task is to find maximum profit value when you can buy stock and sell it with maximum profit.
# it should be borne in mind that you can only calculate the profit by selling in the days following the purchase
#
# Example:
# [2,1,5,6,7,3,4] response should be 6. Because you can buy with price 1 and sell with price 7.

class MaximumProfitSolution:

    def calculate(self, prices: List[int]) -> int:
        # Check if prices array is empty or has one element
        if len(prices) <= 1:
            return 0
        buy = 0
        max_prof = 0
        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_prof = max(max_prof, profit)
            else:
                buy = sell
        return max_prof


max_profit = MaximumProfitSolution()

prices_array = [2, 1, 5, 6, 7, 3, 4]  # 6
out = (max_profit.calculate(prices_array))
print(out)

prices_array = [7, 1, 5, 3, 6, 4]
out = (max_profit.calculate(prices_array))  # 5
print(out)

prices_array = [7, 6, 4, 3, 1]
out = (max_profit.calculate(prices_array))  # 0
print(out)

