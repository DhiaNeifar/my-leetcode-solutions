class Solution {
public:
    int minDeletion(string s, int k) {
        int arr[26] = {0};
        
        for(auto& ch: s){
            arr[ch - 'a']++;
        }

        vector<int> table;
        for(int i = 0; i < 26; i++){
            if(arr[i] > 0){
                table.push_back(arr[i]);
            }
        }
        sort(table.begin(), table.end());

        int total_sum = 0;
        if (k >= table.size())
            return 0;
        for(int i = 0; i < table.size() - k; i++)
            total_sum += table[i];
        
        return total_sum;
    }
};