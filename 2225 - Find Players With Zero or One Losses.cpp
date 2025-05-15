class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        int winners[100001] = {0};
        int losers[100001] = {0};

        for(int i = 0; i < matches.size(); i++){
            winners[matches[i][0]]++;
            losers[matches[i][1]]++;
        }

        vector<int> NeverLost;
        vector<int> LostOnce;

        for(int i = 1; i < 100001; i++){
            if(winners[i] > 0 && losers[i] == 0){
                NeverLost.push_back(i);
            }
            if(losers[i] == 1){
                LostOnce.push_back(i);
            }
        }
        vector<vector<int>> result;
        result.push_back(NeverLost);
        result.push_back(LostOnce);
        return result;
    }
};