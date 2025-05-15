class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int k = 0;
        while(i < nums.size()){
            if(nums[i] == val){k++;}
            else{nums[i - k] = nums[i];}
            i++;
        }
        return i - k; 
    }
};