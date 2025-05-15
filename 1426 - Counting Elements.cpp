class Solution {
public:
    int countElements(vector<int>& arr) {
        int freq[1001] = {0};
        for(auto& el: arr)
            freq[el]++;
        int result = 0;
        for(int i = 0; i < 1000; i++){
            if(freq[i + 1] > 0)
                result += freq[i];
        }
        return result;
    }
};