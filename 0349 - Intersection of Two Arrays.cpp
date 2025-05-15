class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int arr[1001] = {0};
        unordered_set<int> seen;
        vector<int> result;
        for(int i = 0; i < nums1.size(); i++){
            arr[nums1[i]] = 1;
        }
        for(int i = 0; i < nums2.size(); i++){
            if(arr[nums2[i]] == 1)
                seen.insert(nums2[i]);
        }
        for(auto& num: seen){
            result.push_back(num);
        }
        return result;
    }
};