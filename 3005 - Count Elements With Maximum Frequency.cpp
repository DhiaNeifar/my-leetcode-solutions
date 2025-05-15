class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int array[101] = {0};
        int maximum_frequency = 0;
        for(auto& num: nums){
            array[num]++;
            maximum_frequency = max(maximum_frequency, array[num]);
        }
        int result = 0;
        for(int i = 0; i < 101; i++){
            if(array[i] == maximum_frequency)
                result++;
        }
        return result * maximum_frequency;
    }
};