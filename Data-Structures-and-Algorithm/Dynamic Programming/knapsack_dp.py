# -------------------> 0/1 knapsack problem <---------------------------- #

# [P  < -------- capacity (j) ------> ]
#  0   0 | 0   1   2   3   4   5   6   7   8   9   10
#  20  1 | 0  20  20  20  20  20  20  20  20  20   20
#  30  3 | 0  20  20  30  50  50  50  50  50  50   50
#  10  4 | 0  20  20  30  50  50  50  50  60  60   60
#  50  6 | 0  20  20  30  50  50  50  70  70  80  100
# ]

def knapsack(weights, profits, capacity,dp):
    for each_weight in range(1, len(weights)+1):  
        for each_capacity in range(1,capacity+1):
            if weights[each_weight-1] > each_capacity:
                dp[each_weight][each_capacity] = dp[each_weight-1][each_capacity] 
            else:
                dp[each_weight][each_capacity] = max(
                                                    dp[each_weight-1][each_capacity],
                                                    profits[each_weight-1] + 
                                                    dp[each_weight-1][each_capacity-weights[each_weight-1]]
                                                    )       
    return dp 

if __name__ == "__main__" :
    capacity = 10
    weights = [1,3,4,6]
    profits = [20,30,10,50]
    dp = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    knapsack_dp = knapsack(weights, profits, capacity, dp)
    print(knapsack_dp)
    print("The max profit obtained is: ", dp[-1][-1])
    
        
    
    