
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize=2;
    int sum;
    int i,j;
    int *arr_ret=(int*)malloc(sizeof(int)*2);
    for(i=0;i<=numsSize-1;++i)
        for(j=0;j<numsSize;++j)
        {
            if(nums[j]==target-nums[i])
            {
                
                arr_ret[0]=i;
                arr_ret[1]=j;
                break;
                
            } 
            
        }
    return arr_ret;
    
}