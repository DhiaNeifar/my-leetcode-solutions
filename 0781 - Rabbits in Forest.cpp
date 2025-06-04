class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> freq;
        for (auto& answer : answers) {
            freq[answer] += 1;
        }

        int result = 0;
        for (const auto& entry : freq) {
            int answer = entry.first;
            int count = entry.second;
            // Number of groups = ceil(count / (answer + 1)) 
            int group_size = answer + 1;
            int groups = (count + group_size - 1) / group_size;  // ceiling division
            result += groups * group_size;
        }

        return result;
    }
};