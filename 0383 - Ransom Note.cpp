class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        // Make a table size 26 for the frequency of each letter from ransomNote
        // Make a table size 26 for the frequency of each letter from magazine
        // Compare element wise

        vector<int> ransomfreq(26, 0);
        vector<int> magazinefreq(26, 0);
        for(int i = 0; i < ransomNote.size(); i++){ransomfreq[ransomNote[i] - 'a']++;}
        for(int i = 0; i < magazine.size(); i++){magazinefreq[magazine[i] - 'a']++;}
        for(int i = 0; i < 26; i++){
            if (ransomfreq[i] > magazinefreq[i]) return 0;
        }
        return 1;
        }
};