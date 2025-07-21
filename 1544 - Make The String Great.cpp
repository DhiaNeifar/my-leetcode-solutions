class Solution {
public:
    string makeGood(string s) {
        stack<char> result;
        for(auto& character: s){
            if(!result.empty() && (('a' <= result.top() && result.top() <= 'z' && 'A' <= character && character <= 'Z' && character - 'A' + 'a' == result.top()) || ('A' <= result.top() && result.top() <= 'Z' && 'a' <= character && character <= 'z' && character - 'a' + 'A' == result.top()))){
                result.pop();
            }else
                result.push(character);
        }
        string result_string = "";
        while(!result.empty()){
            result_string += result.top();
            result.pop();
        }
        reverse(result_string.begin(), result_string.end());
        return result_string;
    }
};