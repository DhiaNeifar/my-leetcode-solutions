class Solution {
public:
    int findLucky(vector<int>& arr) {
        int tracker[501] = {0};
        for(auto& num : arr)
            tracker[num]++;
        int lucky = -1;
        for(int i = 1; i < 501; i++){
            if(tracker[i] == i)
                lucky = max(lucky, i);
        }
        return lucky;
    }
};