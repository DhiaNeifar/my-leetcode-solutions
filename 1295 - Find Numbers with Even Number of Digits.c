int findNumbers(int* nums, int numsSize) {
    int result = 0;
    for(int i = 0; i < numsSize; i++){
        int number_digits = 0;
        while(nums[i]){
            nums[i] /= 10;
            number_digits++;
        }
        if(number_digits % 2 == 0)result++;
    }
    return result;
}