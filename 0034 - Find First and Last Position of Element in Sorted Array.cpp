class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int begin = nums.size(), end = -1;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == target){
                begin = min(begin, i);
                end = max(end, i);
            }
        }
        vector<int> result = {begin, end};
        if(begin == nums.size()){
            result[0] = -1;
            result[1] = -1;
        }
        return result;
    }
};

 /* private:
    int binary_search(vector<int> arr, int start, int end, int val){
        if(arr[start] == val)
            return start;
        if(arr[end] == val)
            return end;
        while(start <= end){
            int mid = (end - start) / 2;
            if(arr[mid] == val)
                return mid;
            if(arr[mid] < val)
                begin = mid + 1;
            if(arr[mid] > val)
                end = mid - 1;
        }
        return -1;
    }
*/