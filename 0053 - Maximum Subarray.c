int maxSubArray(int* nums, int numsSize){
    int sumlocal = nums[0];
    int sumglobal = nums[0];

    if (numsSize == 1)
    {
        return nums[0];
    }
    else
    {
        for (int i = 1; i < numsSize; i++)
        {   
            if (nums[i] < sumlocal + nums[i])
            {
                sumlocal =  sumlocal + nums[i];
            }
            else
            {
                sumlocal = nums[i];
            }
            if (sumglobal < sumlocal)
            {
                sumglobal =  sumlocal;
            }
        }
        return sumglobal;
    }
}