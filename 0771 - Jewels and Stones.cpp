class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int int_jewels[52] = {0};
        for(auto& ch: jewels){
            if (ch <= 'Z')
                int_jewels[ch - 'A'] = 1;
            if ('a' <= ch)
                int_jewels[ch - 'a' + 26] = 1;
        }
        
        int count[52] = {0};
        for(auto& ch: stones){
            if (ch <= 'Z' && int_jewels[ch - 'A'] != 0)
                count[ch - 'A']++;
            if ('a' <= ch && int_jewels[ch - 'a' + 26] != 0)
                count[ch - 'a' + 26]++;
        }
        int result = 0;
        for(int i = 0; i < 52; i++){
            result += count[i];
        }
        return result;
    }
};