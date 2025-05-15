class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> arr = profit(prices);
        return arr[0];
    }

private:
    vector<int> profit(vector<int>& prices){
        int profit = 0;
        vector<int> result;
        result.push_back(profit);
        if(prices.size() < 2)
            return result;
        
        int buy_index = 0, sell_index = 1;
        int buy = prices[0], sell;
        
        for(int i = 1; i < prices.size(); i++){
            sell = prices[i];
            if(profit < sell - buy){
                profit = sell - buy;
                sell_index = i;
            }
            if(sell < buy){
                buy = sell;
                buy_index = i;
            }
        }

        result[0] = profit;
        result.push_back(buy_index);
        result.push_back(sell_index);
        return result;
    }
};