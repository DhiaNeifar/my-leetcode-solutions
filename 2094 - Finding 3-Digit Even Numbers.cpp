class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> solutions;
        int solution;
        sort(digits.begin(), digits.end());
        for(int i = 0; i < digits.size(); i++)
            cout << digits[i] << "\n";
        for(int i = 0; i < digits.size(); i++){
            for(int j = 0; j < digits.size(); j++){
                for(int k = 0; k < digits.size(); k++){
                    solution = 100 * digits[i] + 10 * digits[j] + digits[k];
                    if(100 <= solution && solution % 2 == 0 && i != j && j != k && i != k)
                        solutions.push_back(solution); 
                }
            }
        }

        if(solutions.size() == 0)
            return solutions;

        sort(solutions.begin(), solutions.end());
        vector<int> filtered_solutions;
        filtered_solutions.push_back(solutions[0]);
        for(int i = 1; i < solutions.size(); i++){
            if(solutions[i] != filtered_solutions[filtered_solutions.size() - 1])
                filtered_solutions.push_back(solutions[i]);
        }
        return filtered_solutions;        
    }
};