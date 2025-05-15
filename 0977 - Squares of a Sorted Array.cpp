class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int neg = 0;
        while (neg < nums.size() && nums[neg] < 0) {
            neg++;
        }

        vector<int> negatives;
        for (int i = neg - 1; i >= 0; i--) {
            negatives.push_back(-nums[i]); // reversed and negated to make ascending
        }

        vector<int> result;
        int i = 0, j = neg; // i for negatives, j for non-negatives in original nums

        while (i < negatives.size() && j < nums.size()) {
            if (negatives[i] < nums[j]) {
                result.push_back(negatives[i] * negatives[i]);
                i++;
            } else {
                result.push_back(nums[j] * nums[j]);
                j++;
            }
        }

        while (i < negatives.size()) {
            result.push_back(negatives[i] * negatives[i]);
            i++;
        }

        while (j < nums.size()) {
            result.push_back(nums[j] * nums[j]);
            j++;
        }

        return result;
    }
};