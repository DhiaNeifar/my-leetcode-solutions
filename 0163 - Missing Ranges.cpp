class Solution {
public:
    vector<vector<int>> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<vector<int>> result;
        if(nums.size() == 0){
            vector<int> v = {lower, upper};
            result.push_back(v);
            return result;
        }       

        if(lower < nums[0]){
            vector<int> v;
            v.push_back(lower);
            v.push_back(nums[0] - 1);
            result.push_back(v);
        }
    
        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] < nums[i + 1] - 1){
                vector<int> v;
                v.push_back(nums[i] + 1);
                v.push_back(nums[i + 1] - 1);
                result.push_back(v);
            }
        }
        if(nums[nums.size() - 1] < upper){
            vector<int> v;
            v.push_back(nums[nums.size() - 1] + 1);
            v.push_back(upper);
            result.push_back(v);
        }
        return result;
    }
};