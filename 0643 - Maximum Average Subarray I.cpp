class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double window = 0;
        for(int i = 0; i < k; i++){
            window += nums[i];
        }
        double result = window;
        for(int i = 1; i < nums.size() - k + 1; i++){
            window -= nums[i - 1];
            window += nums[i + k - 1];
            result = max(window, result);
        }
        return result / k;
    }
};