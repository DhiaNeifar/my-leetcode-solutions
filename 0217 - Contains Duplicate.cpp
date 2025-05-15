class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> tracker;
        for(int i = 0; i < nums.size(); i++){
            if(tracker.contains(nums[i])) return true;
            tracker[nums[i]] = 1;
        }
        return false;
    }
};