int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int consecutives[numsSize + 1];
    for (int i = 0; i < numsSize + 1; i++) {consecutives[i] = 0;}
    int max_consecutive = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == 1){
            consecutives[i + 1] = consecutives[i] + 1;
            if(consecutives[i + 1] > max_consecutive){max_consecutive = consecutives[i + 1];}
        }else{consecutives[i + 1] = 0;}
    }
    return max_consecutive;
}