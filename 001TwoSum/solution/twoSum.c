#include <stdio.h>

int result[2];

void twoSum(int* nums, int numsSize, int target) {
    for (int i =0; i < numsSize; i++){
        for (int j = i+1; j < numsSize; j++){
            printf("i=%d\n",i);
            printf("j=%d\n",j);
            int num1 = *(nums+i);
            int num2 = *(nums+j);
            printf("i=%d\n",num1);
            printf("j=%d\n",num2);
            if (num1+num2== target){
                *result = i; 
                *(result+1) = j; 
                printf("Found\n");
                //return *result;        
            }
            else
                printf("Next\n");
        }
    }
}

int main() {

    int nums[] = {2, 7, 11, 15};
    int numsSize = 4;
    int target = 26;



    twoSum(nums,numsSize,target);
    //printf("num1=%d",target);
    printf("num1=%d,num2=%d",*result,*(result+1));
    return 1;
}
