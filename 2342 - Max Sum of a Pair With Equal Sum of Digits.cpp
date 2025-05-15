class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int, vector<int>> tracker;
        for(int i = 0; i < nums.size(); i++){
            int sum_digits = 0;
            int num_copy = nums[i];
            while(num_copy){
                sum_digits += num_copy % 10;
                num_copy /= 10;
            }
            tracker[sum_digits].push_back(nums[i]);
        }
        int result = -1;
        for (auto& [key, value] : tracker){
            if(value.size() >= 2){
                sort(value.begin(), value.end());
                result = max(result, value[value.size() - 1] + value[value.size() - 2]);
            }
        }
        return result;
    }
};