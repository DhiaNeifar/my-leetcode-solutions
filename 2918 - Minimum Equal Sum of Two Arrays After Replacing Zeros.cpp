class Solution {
public:
    long long minSum(vector<int>& nums1, vector<int>& nums2) {
        int zeros1 = 0, zeros2 = 0;
        long long sum1 = 0, sum2 = 0;

        for(auto& num: nums1){
            if(num == 0)
               zeros1++;
            sum1 += num; 
        }

        for(auto& num: nums2){
            if(num == 0)
               zeros2++;
            sum2 += num; 
        }

        if (zeros1 > 0 && zeros2 > 0)
            return max(sum1 + zeros1, sum2 + zeros2); 

        if (zeros1 > 0 && zeros2 == 0){
            if(sum1 + zeros1 > sum2) 
                return -1;
            else 
                return sum2;
        }

        if (zeros2 > 0 && zeros1 == 0){
            if(sum2 + zeros2 > sum1) 
                return -1;
            else 
                return sum1;
        }

        if (zeros1 == 0 && zeros2 == 0 and sum1 == sum2)
            return sum1;
        else
            return -1;
    }
};