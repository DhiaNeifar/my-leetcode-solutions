class Solution {
public:
    char repeatedCharacter(string s) {
        int frequency[26] = {0};
        for(auto& ch: s){
            if (frequency[ch - 'a']){
                return ch;
            }else {frequency[ch - 'a']++;}
        }
    return 0;
    }
};