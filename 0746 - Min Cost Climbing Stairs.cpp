class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp;
        
        dp.push_back(cost[0]);
        dp.push_back(cost[1]);
        
        for(int i = 2; i < cost.size(); i++)
            dp.push_back(min(dp[dp.size() - 1], dp[dp.size() - 2]) + cost[i]);
        
        return min(dp[dp.size() - 1], dp[dp.size() - 2]);
    }
};