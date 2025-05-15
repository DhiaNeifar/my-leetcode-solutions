class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        int seen[1000001] = {0};
        int last_seen[1000001] = {0};
        int optimal = 1000001;
        for(int i = 0; i < cards.size(); i++){
            if (seen[cards[i]] > 0){
                optimal = min(optimal, i - last_seen[cards[i]] + 1);
            }
            seen[cards[i]]++;
            last_seen[cards[i]] = i;
        }
        return optimal == 1000001 ? -1 : optimal;
    }
};