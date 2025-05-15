class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        long long arr[26] = {0};
        long long result = 0;
        const long long div = 1000000007;

        for (char ch : s)
            arr[ch - 'a']++;

        while (t--) {
            long long nxt[26] = {0};
            nxt[0] = arr[25] % div;
            nxt[1] = (arr[25] + arr[0]) % div;
            for (int i = 2; i < 26; ++i) {
                nxt[i] = arr[i - 1] % div;
            }
            for (int i = 0; i < 26; ++i) {
                arr[i] = nxt[i];
            }
        }

        for (int i = 0; i < 26; ++i) {
            result = (result + arr[i]) % div;
        }
        return result;
    }
};