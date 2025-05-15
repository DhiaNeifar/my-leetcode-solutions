class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first_occurance = binary_search(nums, 0, nums.size() - 1, target);          
        vector<int> result;

        result.push_back(first_occurance);
        result.push_back(first_occurance);
        
        if(first_occurance == -1){
            return result;
        }

        int i = first_occurance, j = first_occurance;
        while(i >= 0 && nums[i] == target){
            i--;
        }
        
        while(j < nums.size() && nums[j] == target){
            j++;
        }

        result[0] = i + 1;
        result[1] = j - 1;
        return result;
    }

private:
    int binary_search(vector<int> arr, int start, int end, int val){
        while(start <= end){
            int mid = (end + start) / 2;
            if(arr[mid] == val)
                return mid;
            if(arr[mid] < val)
                start = mid + 1;
            if(arr[mid] > val)
                end = mid - 1;
        }
        return -1;
    }
};