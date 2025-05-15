class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        int arr[1001] = {0};
        for(auto& vect: nums){
            for(auto& num: vect)
                arr[num]++;
        }
        vector<int> result;
        for(int i = 1; i < 1001; i++){
            if(arr[i] == nums.size())
                result.push_back(i);
        }
        return result;
    }
};