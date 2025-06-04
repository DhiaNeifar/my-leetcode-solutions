class Solution {
public:
    int countLargestGroup(int n) {
        int array[37];
        for(int i = 0; i < 37; i++) {
            array[i] = 0;
        }

        for(int i = 1; i <= n; i++) {
            int sum_digits = 0, temp = i;
            while(temp != 0) {
                sum_digits += temp % 10;
                temp /= 10;
            }
            array[sum_digits]++;
        } 

        int curr_max = array[0];
        int occurence = 1;
        for(int i = 1; i < 37; i++) {
            if(array[i] == curr_max)
                occurence++;
            if(array[i] > curr_max){
                curr_max = array[i];
                occurence = 1;
            }
        }

        return occurence;  
    }
};