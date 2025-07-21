class Solution {
public:
    int maxDifference(string s) {
        int arr[26] = {0};
        int max_odd = 1; 
        int min_even = s.size();
        for(char character: s){
            int index = character - 'a';
            arr[index]++;
        }
        for(char character: s){
            int index = character - 'a';
            if (arr[index] % 2 == 0 && arr[index] < min_even) min_even = arr[index];
            if (arr[index] % 2 == 1 && arr[index] > max_odd) max_odd = arr[index]; 
        }
        return max_odd - min_even;
    }
};