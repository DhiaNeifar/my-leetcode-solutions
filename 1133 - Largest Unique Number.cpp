class Solution {
public:
    int largestUniqueNumber(vector<int>& nums) {
        int freq[1001] = {0};
        for(auto& num: nums)
            freq[num]++;
        
        sort(nums.begin(), nums.end());
        for(int i = nums.size() - 1; i >= 0; i--){
            if(freq[nums[i]] == 1)
                return nums[i];
        }
        return -1;
    }
};