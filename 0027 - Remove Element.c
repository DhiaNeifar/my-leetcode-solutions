int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    int k = 0;
    while(i < numsSize){
        if(nums[i] == val){k++;}
        else{nums[i - k] = nums[i];}
        i++;
    }
    return i - k;
}