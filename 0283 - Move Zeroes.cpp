class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, zeros = 0;
        while(i + zeros < nums.size()){
            if(nums[i + zeros] == 0){zeros++;}else{nums[i] = nums[i + zeros]; i++;}
        }
        while(zeros){nums[nums.size() - zeros] = 0; zeros--;}
    }
};