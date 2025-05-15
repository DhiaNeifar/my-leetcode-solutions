class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        int array[101] = {0};
        int result = 0;
        for(auto& num: nums){
            if(array[num] == 0){
                result += num;
            }
            if(array[num] == 1){
                result -= num;
            }
            array[num]++;
        }
        return result;
    }
};