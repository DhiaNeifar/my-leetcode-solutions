class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> path_finder;
        for(auto& path: paths){
            path_finder[path[0]] = path[1];
        }
        string starting_point = paths[0][0];
        while(path_finder.contains(starting_point))
            starting_point = path_finder[starting_point];
        return starting_point;
    }   
};