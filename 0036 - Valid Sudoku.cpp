class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int offset = '1';
        int num;
        for(int i = 0; i < 9; i++){
            vector<int> seen_row = init_seen(), seen_col = init_seen();
            for(int j = 0; j < 9; j++){
                // Columns
                if(board[i][j] != '.'){
                    num = board[i][j] - offset;
                    if (seen_col[num] > 0) return false;
                    seen_col[num]++;
                }
                // Rows
                if(board[j][i] != '.'){
                    num = board[j][i] - offset;
                    if (seen_row[num] > 0) return false;
                    seen_row[num]++;
                }
            }
        }
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                // 3x3 Grid
                vector<int> seen_grid = init_seen();
                for(int k = 3 * i; k < 3 * i + 3; k++){
                    for(int l = 3 * j; l < 3 * j + 3; l++){
                        if(board[k][l] != '.') {
                            num = board[k][l] - offset;
                            if (seen_grid[num] > 0) return false;
                            seen_grid[num]++;
                        }
                    }
                }
            }
        }
        return true;
    }
private:
    vector<int> init_seen(){
        return vector<int>(9, 0);
    }
};