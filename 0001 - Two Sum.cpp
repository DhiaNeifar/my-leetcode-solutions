class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> our_map;
        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            int difference = target - nums[i];
            if(our_map.find(difference) != our_map.end()){
                result.push_back(i);
                result.push_back(our_map[difference]);
                return result;
            }else our_map[nums[i]] = i;
        }
        return result;
    }
};