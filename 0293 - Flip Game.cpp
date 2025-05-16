class Solution {
public:
    vector<string> generatePossibleNextMoves(string currentState) {
        vector<string> result;
        if(currentState.size() == 1)
            return result;

        for(int i = 0; i < currentState.size() - 1; i++){
            if(currentState[i] == '+' && currentState[i + 1] == '+'){
                result.push_back(currentState);
                result[result.size() - 1][i] = '-';
                result[result.size() - 1][i + 1] = '-';
            }
        }
        return result;
    }
};