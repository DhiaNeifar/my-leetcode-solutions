class Solution {
public:
    bool isValid(string s) {
        vector<char> anticlockwise = {'(', '[', '{'};
        vector<char> clockwise = {')', ']', '}'};
        
        stack<int> parentheses;

        for(auto& character: s){
            if(character )
            if(find(anticlockwise.begin(), anticlockwise.end(), character) != anticlockwise.end()){
                parentheses.push(character);
            }
            auto it = find(clockwise.begin(), clockwise.end(), character);
            if(it != clockwise.end()){
                int index = it - clockwise.begin();
                if(parentheses.empty() || parentheses.top() != anticlockwise[index]) return false;
                parentheses.pop();
             }
        }
        return parentheses.empty();
    }
};