class Solution {
public:
    int maxSubstrings(string word) {
        if(word.size() < 4) return 0;
        vector<int> last_seen = InitLastSeenArray();
        int result = 0, char_index;

        for(int i = 0; i < word.size(); i++){
            char_index = word[i] - 'a';
            if(last_seen[char_index] == -1){
                last_seen[char_index] = i;
            }else if(i - last_seen[char_index] + 1 > 3){
                result++;
                last_seen = InitLastSeenArray();
            }
        }
        return result;
    }
private:
    vector<int> InitLastSeenArray(){
        return vector<int>(26, -1);
    }
};