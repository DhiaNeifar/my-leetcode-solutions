class Solution {
public:
    bool validPalindrome(string s) {
        int start = 0, end = s.size() - 1;
        while (start < end) {
            if (s[start] != s[end]) {
                // Skip one character from either side and check again
                return isPalindrome(s, start + 1, end) || isPalindrome(s, start, end - 1);
            }
            start++;
            end--;
        }
        return true;
    }

private:
    bool isPalindrome(const string& s, int left, int right) {
        while (left < right) {
            if (s[left++] != s[right--]) return false;
        }
        return true;
    }
};