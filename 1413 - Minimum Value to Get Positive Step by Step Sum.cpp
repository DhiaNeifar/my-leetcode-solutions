class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int minimum = nums[0];
        for (int i = 1; i < nums.size(); i++){
            nums[i] += nums[i - 1];
            minimum = min(minimum, nums[i]); 
        }
        return max(1, 1 - minimum);
    }
};