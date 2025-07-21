class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        if (nums.size() == 1) return true;

        bool prev = nums[0] & 1;
        for (int i = 1; i < nums.size(); i++){
            bool curr = nums[i] & 1;
            if (prev == curr) return false;
            prev = curr;
        }
        return true;
    }
};