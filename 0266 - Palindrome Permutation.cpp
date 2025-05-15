class Solution {
public:
    bool canPermutePalindrome(string s) {
        int arr[26] = {0};
        for(auto& ch: s)
            arr[ch - 'a']++;
        int odds = 0;
        for(int i = 0; i < 26; i++){
            if(arr[i] % 2 == 1)
                odds++;
        }
        if(odds > 1 || (odds == 1 && s.size() % 2 == 0))
            return false;
        
        return true;
    }
};