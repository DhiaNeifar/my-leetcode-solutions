class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
        if(nums.size() == 1)
            return nums[0];
        int freq[1001] = {0};
        for(auto& num: nums)
            freq[num]++;
        if(nums.size() == 1)
            return true; 
        sort(nums.begin(), nums.end());
        for(int i = nums.size() - 1; i >= 0; i--){
            if(freq[nums[i]] == 1)
                return nums[i];
        }
        return -1;
    }
};