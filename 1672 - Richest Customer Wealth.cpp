class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        double max_wealth = 0;
        double customer_wealth;
        for(int i = 0; i < accounts.size(); i++){
            customer_wealth = 0;
            for(int j = 0; j < accounts[i].size(); j++){
                customer_wealth += accounts[i][j];
            }
            if (customer_wealth > max_wealth) max_wealth = customer_wealth;
        }
        return max_wealth; 
    }
};