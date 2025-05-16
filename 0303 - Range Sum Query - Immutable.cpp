class NumArray {
private:
    vector<int> numarray;
public:
    NumArray(vector<int>& nums) {
        numarray = nums;
    }
    
    int sumRange(int left, int right) {
        int result = 0;
        for(int i = left; i <= right; result += numarray[i], i++);
        return result;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */