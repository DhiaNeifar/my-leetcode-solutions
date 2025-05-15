class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_consecutive = nums[0];
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == 1){
                nums[i] = nums[i - 1] + 1;
                max_consecutive = max(nums[i], max_consecutive);
            }
        }
        return max_consecutive;
    }
};