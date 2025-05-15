class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        vector<long long>rows, columns;

        long long row_sum = 0, column_sum = 0;
        
        for(int i = 0; i < m; i++){
            row_sum = 0;
            for(int j = 0; j < n; j++){
                row_sum += grid[i][j];
            }
            rows.push_back(row_sum);
        }
        
        for(int j = 0; j < n; j++){
            column_sum = 0;
            for(int i = 0; i < m; i++){
                column_sum += grid[i][j];
            }
            columns.push_back(column_sum);
        }
        long long total_sum = accumulate(rows.begin(), rows.end(), 0LL);
        if (total_sum % 2 != 0) return false;
        
        long long half_total_sum = total_sum / 2;
    
        long long prefix_row_sum = 0;
        for(auto& num: rows){
            prefix_row_sum += num;
            if(prefix_row_sum == half_total_sum)
                return true;
        }

        long long prefix_column_sum = 0;
        for(auto& num: columns){
            prefix_column_sum += num;
            if(prefix_column_sum == half_total_sum)
                return true;
        }

        return false;
    }
};