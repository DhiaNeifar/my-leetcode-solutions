class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int duplicates = 0;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i - 1] == nums[i]){duplicates++;}
            nums[i - duplicates] = nums[i];
        }
        return nums.size() - duplicates;
    }
};