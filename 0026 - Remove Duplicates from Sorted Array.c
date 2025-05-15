int removeDuplicates(int* nums, int numsSize) {
    int duplicates = 0;
    for(int i = 1; i < numsSize; i++){
        if(nums[i - 1] == nums[i]){duplicates++;}
        nums[i - duplicates] = nums[i];
    }
    return numsSize - duplicates;
}