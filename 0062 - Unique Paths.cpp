class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<std::vector<int>> arr(m, std::vector<int>(n, 1));
        
        if(m == 1 || n == 1)
            return 1;

        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1];
            }
        }
        return arr[m - 1][n - 1];
    }
};