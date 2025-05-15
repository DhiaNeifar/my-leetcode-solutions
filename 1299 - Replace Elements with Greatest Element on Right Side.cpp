class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int arr_length = arr.size() - 1;
        int curr_max = -1;
        int placeholder = arr[arr_length];
        arr[arr_length] = curr_max;
        for(int i = arr_length - 1; i >= 0; i--){
            curr_max = max(curr_max, placeholder);
            placeholder = arr[i];
            arr[i] = curr_max;
        }
        return arr;
    }
};