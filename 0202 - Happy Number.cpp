class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;
        while (true){
            int t = DigitSum(n);
            if(seen.contains(t))
                return false;
            if(t == 1)
                return true;
            seen.insert(t);
            n = t;
        }
    }

private:
    int DigitSum(int n){
        int digitsum = 0;
        while(n){
            int rest = n % 10;
            digitsum += rest * rest;
            n /= 10;
        }
        return digitsum;
    }
};