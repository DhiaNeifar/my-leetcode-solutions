class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        int arr1[1001] = {0};
        int arr2[1001] = {0};
        vector<int> result;
        for(int i = 0; i < nums1.size(); i++){
            arr1[nums1[i]]++;
        }
        for(int i = 0; i < nums2.size(); i++){
            arr2[nums2[i]]++;
        }

        for(int i = 0; i < 1001; i++){
            for(int j = 0; j < min(arr1[i], arr2[i]); j++)
                result.push_back(i);
        }
        return result;
    }
};