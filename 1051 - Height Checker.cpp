class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> heights_copy = heights;
        sort(heights_copy.begin(), heights_copy.end());
        int unexpected = 0;
        for(int i = 0; i < heights.size(); i++){
            if(heights[i] != heights_copy[i]) unexpected++;
        }
        return unexpected;
    }
};