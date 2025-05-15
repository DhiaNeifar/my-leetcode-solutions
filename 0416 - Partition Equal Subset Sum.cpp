class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int half_sum = 0;
        for(int i = 0; i < nums.size(); i++)
            half_sum += nums[i];
        
        if(nums.size() == 1 || half_sum % 2 == 1){
            return false;
        }

        half_sum /= 2;
        unordered_set<int> set;
        set.insert(0);
        for(auto& num: nums){
            unordered_set<int> next_set = set;
            for(auto& already_seen : set){
                int result = num + already_seen;
                if(result == half_sum)
                    return true;
                next_set.insert(result);
            }
            set = next_set;
        }
        return false;
    }
};