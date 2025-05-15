class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        long int window = 0;
        vector<int> result;
        int i = 0;
        while(i < nums.size()){
            if(i - k < 0 || i + k >= nums.size()){
                result.push_back(-1);
            }else{
                if(window == 0){
                    for(int j = i - k; j < i + k + 1; j++){
                        window += nums[j];
                    }
                }else{
                    window -= nums[i - k - 1];
                    window += nums[i + k];
                }
                result.push_back(window / (2 * k + 1));
            }
            i++;
        }
        return result;
    }
};